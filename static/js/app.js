var sessionId = null;

var SUGGESTIONS = [
  "Show distribution of numeric columns",
  "Which category has the highest average?",
  "Plot a correlation heatmap",
  "Show trends over time",
  "Top 10 rows by value",
  "Describe the dataset"
];

var uploadPanel  = document.getElementById("upload-panel");
var schemaPanel  = document.getElementById("schema-panel");
var chatPanel    = document.getElementById("chat-panel");
var dropZone     = document.getElementById("drop-zone");
var fileInput    = document.getElementById("file-input");
var uploadStatus = document.getElementById("upload-status");
var schemaStats  = document.getElementById("schema-stats");
var previewWrap  = document.getElementById("preview-wrap");
var schemaText   = document.getElementById("schema-text");
var datasetMeta  = document.getElementById("dataset-meta");
var messages     = document.getElementById("messages");
var qInput       = document.getElementById("q-input");
var sendBtn      = document.getElementById("send-btn");
var chips        = document.getElementById("chips");
var overlay      = document.getElementById("overlay");
var changeBtn    = document.getElementById("change-btn");

fileInput.addEventListener("change", function() {
  if (fileInput.files[0]) uploadFile(fileInput.files[0]);
});

dropZone.addEventListener("dragover", function(e) {
  e.preventDefault();
  dropZone.classList.add("drag-over");
});
dropZone.addEventListener("dragleave", function() {
  dropZone.classList.remove("drag-over");
});
dropZone.addEventListener("drop", function(e) {
  e.preventDefault();
  dropZone.classList.remove("drag-over");
  if (e.dataTransfer.files[0]) uploadFile(e.dataTransfer.files[0]);
});

changeBtn.addEventListener("click", function() {
  schemaPanel.classList.add("hidden");
  chatPanel.classList.add("hidden");
  uploadPanel.classList.remove("hidden");
  uploadStatus.classList.add("hidden");
  messages.innerHTML = "";
  chips.innerHTML = "";
  datasetMeta.textContent = "";
  sessionId = null;
  sendBtn.disabled = true;
});

function showStatus(msg, type) {
  uploadStatus.textContent = msg;
  uploadStatus.className = "status" + (type ? " " + type : "");
  uploadStatus.classList.remove("hidden");
}

function uploadFile(file) {
  showStatus("Uploading…", "");
  var formData = new FormData();
  formData.append("file", file);

  fetch("/upload", { method: "POST", body: formData })
    .then(function(res) { return res.json(); })
    .then(function(data) {
      if (data.error) { showStatus(data.error, "error"); return; }

      sessionId = data.session_id;

      schemaStats.innerHTML =
        '<span class="stat-chip"><strong>' + data.rows.toLocaleString() + '</strong> rows</span>' +
        '<span class="stat-chip"><strong>' + data.columns + '</strong> columns</span>' +
        '<span class="stat-chip"><strong>' + esc(file.name) + '</strong></span>';

      if (data.preview && data.preview.length) {
        var cols = Object.keys(data.preview[0]);
        var html = "<table><thead><tr>" + cols.map(function(c) { return "<th>" + esc(c) + "</th>"; }).join("") + "</tr></thead><tbody>";
        data.preview.forEach(function(row) {
          html += "<tr>" + cols.map(function(c) { return '<td title="' + esc(String(row[c] != null ? row[c] : "")) + '">' + esc(String(row[c] != null ? row[c] : "")) + "</td>"; }).join("") + "</tr>";
        });
        html += "</tbody></table>";
        previewWrap.innerHTML = html;
      }

      schemaText.textContent = data.schema || "";
      datasetMeta.textContent = file.name + " · " + data.rows.toLocaleString() + " rows · " + data.columns + " cols";

      uploadPanel.classList.add("hidden");
      schemaPanel.classList.remove("hidden");
      chatPanel.classList.remove("hidden");
      sendBtn.disabled = false;

      renderChips(data.column_names || []);
      showStatus("Dataset loaded successfully!", "success");
      setTimeout(function() { uploadStatus.classList.add("hidden"); }, 3000);
    })
    .catch(function(err) { showStatus("Network error: " + err.message, "error"); });
}

function renderChips(colNames) {
  chips.innerHTML = "";
  var all = SUGGESTIONS.slice(0, 4).concat(colNames.slice(0, 3).map(function(c) { return "Distribution of " + c; })).slice(0, 7);
  all.forEach(function(text) {
    var btn = document.createElement("button");
    btn.className = "chip";
    btn.textContent = text;
    btn.onclick = function() { qInput.value = text; autoResize(); sendBtn.disabled = false; send(); };
    chips.appendChild(btn);
  });
}

qInput.addEventListener("input", function() {
  autoResize();
  sendBtn.disabled = !qInput.value.trim() || !sessionId;
});

qInput.addEventListener("keydown", function(e) {
  if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); if (!sendBtn.disabled) send(); }
});

sendBtn.addEventListener("click", send);

function autoResize() {
  qInput.style.height = "auto";
  qInput.style.height = Math.min(qInput.scrollHeight, 130) + "px";
}

function send() {
  var q = qInput.value.trim();
  if (!q || !sessionId) return;
  qInput.value = "";
  qInput.style.height = "auto";
  sendBtn.disabled = true;

  appendUserMsg(q);
  overlay.classList.remove("hidden");

  fetch("/ask", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ session_id: sessionId, question: q })
  })
  .then(function(res) { return res.json(); })
  .then(function(data) {
    overlay.classList.add("hidden");
    sendBtn.disabled = false;
    if (data.error && !data.explanation && !data.code) {
      appendErrMsg(data.error);
    } else {
      appendBotMsg(data);
    }
    var last = messages.lastElementChild;
    if (last) last.scrollIntoView({ behavior: "smooth", block: "start" });
  })
  .catch(function(err) {
    overlay.classList.add("hidden");
    sendBtn.disabled = false;
    appendErrMsg("Network error: " + err.message);
  });
}

function appendUserMsg(text) {
  var d = document.createElement("div");
  d.className = "msg msg-user";
  d.innerHTML = '<div class="bubble">' + esc(text) + '</div>';
  messages.appendChild(d);
  d.scrollIntoView({ behavior: "smooth", block: "end" });
}

function appendBotMsg(data) {
  var d = document.createElement("div");
  d.className = "msg msg-bot";
  var html = '<div class="bubble">';

  if (data.explanation) {
    html += '<div class="label">Analysis</div><div class="explanation">' + esc(data.explanation) + '</div>';
  }
  if (data.chart_url) {
    html += '<div class="chart-wrap"><img src="' + data.chart_url + '" alt="Chart" loading="lazy"/></div>';
  }
  if (data.output) {
    html += '<pre class="exec-output">' + esc(data.output) + '</pre>';
  }
  if (data.error) {
    html += '<pre class="exec-error">Execution error:\n' + esc(data.error) + '</pre>';
  }
  if (data.insight) {
    html += '<div class="insight-box"><div class="label">Key Insight</div>' + esc(data.insight) + '</div>';
  }
  if (data.code) {
    html += '<details class="code-toggle"><summary>View generated code</summary><pre class="code-block">' + esc(data.code) + '</pre></details>';
  }

  html += '</div>';
  d.innerHTML = html;
  messages.appendChild(d);
}

function appendErrMsg(text) {
  var d = document.createElement("div");
  d.className = "msg msg-bot";
  d.innerHTML = '<div class="bubble"><pre class="exec-error">' + esc(text) + '</pre></div>';
  messages.appendChild(d);
}

function esc(str) {
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}
