import uuid
import os

import pandas as pd
import matplotlib
matplotlib.use("Agg")

from flask import Flask, render_template, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename

from schema import build_schema
from executor import execute_analysis
from copilot import ask_copilot

from dotenv import load_dotenv
load_dotenv()
import os
print("KEY:", os.environ.get("MISTRAL_API_KEY", "NOT FOUND")[:10] + "...")
print("ENV FILE PATH:", os.path.abspath(".env"))

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "datacopilot-secret-2024")

BASE_DIR      = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
CHART_FOLDER  = os.path.join(BASE_DIR, "charts")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CHART_FOLDER,  exist_ok=True)

app.config["MAX_CONTENT_LENGTH"] = 50 * 1024 * 1024

ALLOWED = {"csv", "xlsx", "xls", "json", "parquet"}

# In-memory store: { session_id: {"df": df, "schema": str, "history": [...]} }
STORE = {}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED


def load_df(path, filename):
    ext = filename.rsplit(".", 1)[1].lower()
    if ext == "csv":
        return pd.read_csv(path)
    elif ext in ("xlsx", "xls"):
        return pd.read_excel(path)
    elif ext == "json":
        return pd.read_json(path)
    elif ext == "parquet":
        return pd.read_parquet(path)
    raise ValueError("Unsupported file type: " + ext)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    if not file.filename or not allowed_file(file.filename):
        return jsonify({"error": "Invalid or unsupported file type"}), 400

    filename = secure_filename(file.filename)
    sid      = str(uuid.uuid4())
    save_path = os.path.join(UPLOAD_FOLDER, sid + "_" + filename)
    file.save(save_path)

    try:
        df = load_df(save_path, filename)
    except Exception as e:
        return jsonify({"error": "Could not parse file: " + str(e)}), 400

    schema_str = build_schema(df)
    STORE[sid] = {"df": df, "schema": schema_str, "history": []}

    return jsonify({
        "session_id":   sid,
        "rows":         len(df),
        "columns":      len(df.columns),
        "schema":       schema_str,
        "preview":      df.head(5).to_dict(orient="records"),
        "column_names": df.columns.tolist(),
    })


@app.route("/ask", methods=["POST"])
def ask():
    body     = request.get_json(force=True)
    sid      = body.get("session_id", "")
    question = body.get("question", "").strip()

    if not sid or sid not in STORE:
        return jsonify({"error": "No dataset loaded. Please upload a file first."}), 400
    if not question:
        return jsonify({"error": "Question cannot be empty."}), 400

    store   = STORE[sid]
    df      = store["df"]
    schema  = store["schema"]
    history = store["history"]

    try:
        result = ask_copilot(question, schema, history)
    except Exception as e:
        return jsonify({"error": "Copilot error: " + str(e)}), 500

    explanation = result.get("explanation", "")
    code        = result.get("code", "")
    insight     = result.get("insight", "")
    raw_text    = result.get("raw", "")

    chart_url   = None
    exec_output = ""
    exec_error  = ""

    if code:
        chart_filename = sid + "_" + uuid.uuid4().hex + ".png"
        chart_path_abs = os.path.join(CHART_FOLDER, chart_filename)
        exec_result    = execute_analysis(code, df, chart_path_abs)
        exec_output    = exec_result.get("output", "")
        exec_error     = exec_result.get("error", "")
        if os.path.exists(chart_path_abs):
            chart_url = "/charts/" + chart_filename

    history.append({"role": "user",      "content": question})
    history.append({"role": "assistant", "content": raw_text})
    store["history"] = history[-20:]

    return jsonify({
        "explanation": explanation,
        "code":        code,
        "insight":     insight,
        "chart_url":   chart_url,
        "output":      exec_output,
        "error":       exec_error,
    })


@app.route("/charts/<filename>")
def serve_chart(filename):
    return send_from_directory(CHART_FOLDER, filename)


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
