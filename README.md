# DataCopilot

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue" alt="Python 3.9+">
  <img src="https://img.shields.io/badge/License-GPL--3.0-green" alt="License: GPL-3.0">
  <img src="https://img.shields.io/badge/AI-Mistral%20API-purple" alt="AI: Mistral API">
  <img src="https://img.shields.io/github/stars/Pranish-Sapkota/DataCopilot?style=social" alt="GitHub Stars">
</p>

<p align="center">
  <b>AI-Powered Data Analysis Assistant</b><br>
  Upload your dataset and ask questions in plain English — DataCopilot writes and executes Python analysis code on the fly, delivering charts, computed results, and data-driven insights through an intuitive chat interface.
</p>

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Supported Analysis Types](#supported-analysis-types)
- [Project Structure](#project-structure)
- [Security](#security)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

DataCopilot leverages the [Mistral AI API](https://docs.mistral.ai/) to turn natural language questions into executable Python data analysis. Built on a lightweight Flask backend with a clean vanilla HTML/CSS/JS frontend, it provides an interactive environment for exploring datasets without writing code.

**Live Repository:** [github.com/Pranish-Sapkota/DataCopilot](https://github.com/Pranish-Sapkota/DataCopilot)

---

## Features

- **Drag-and-Drop Upload** — Supports CSV, Excel (`.xlsx` / `.xls`), JSON, and Parquet files.
- **Automatic Schema Detection** — Identifies column types, null counts, sample values, and numeric summaries instantly.
- **Natural Language Q&A** — Ask questions about your data in plain English with full follow-up and contextual support.
- **Auto-Generated Charts** — Produces distribution plots, comparisons, trends, correlations, rankings, and part-of-whole visualizations using Matplotlib and Seaborn.
- **Sandboxed Execution** — All generated code runs in a restricted environment with dangerous imports and built-ins disabled.
- **Conversation Memory** — Maintains session context so follow-up questions like *"now filter to 2023"* work seamlessly.

---

## Demo

1. Upload your dataset.
2. Review the auto-detected schema and preview.
3. Ask questions in the chat.
4. Receive explanations, charts, and insights instantly.

A `sample_data.csv` file is included for quick testing.

---

## Installation

### Prerequisites

- Python 3.9 or higher
- A [Mistral AI API key](https://console.mistral.ai/api-keys) (free tier available)

### Steps

```bash
# Clone the repository
git clone https://github.com/Pranish-Sapkota/DataCopilot.git
cd DataCopilot

# Create and activate a virtual environment
# Windows:
python -m venv venv
venv\Scripts\activate

# macOS / Linux:
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the project root:

```env
MISTRAL_API_KEY=your_mistral_api_key_here
MISTRAL_MODEL=mistral-small-latest
```

> **Important:** Do not add spaces around `=` and do not wrap values in quotes. Both will break the configuration.

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `MISTRAL_API_KEY` | Yes | — | Your Mistral API key |
| `MISTRAL_MODEL` | No | `mistral-small-latest` | Mistral model used for code generation |
| `SECRET_KEY` | No | auto-generated | Flask session secret |

---

## Usage

```bash
python app.py
```

Open [http://localhost:5000](http://localhost:5000) in your browser.

### Example Questions

- *"Show the distribution of Age"*
- *"Compare average revenue by region"*
- *"What's the trend in sales over time?"*
- *"Plot a correlation heatmap"*
- *"Top 10 customers by total spend"*

Continue the conversation naturally:

- *"Make it a bar chart"*
- *"Now filter to 2024 only"*
- *"Add a trend line"*

---

## Supported Analysis Types

| Type | Example | Output |
|------|---------|--------|
| **Distribution** | *"Show the distribution of Age"* | Histogram with mean line |
| **Comparison** | *"Compare sales by category"* | Sorted bar chart |
| **Trend** | *"Revenue trend by month"* | Line chart over time |
| **Relationship** | *"Does price affect rating?"* | Scatter plot with correlation |
| **Correlation Matrix** | *"Show all correlations"* | Heatmap |
| **Ranking** | *"Top 10 products by revenue"* | Horizontal bar chart |
| **Part-of-Whole** | *"Sales breakdown by category"* | Pie or bar chart |
| **Filtering** | *"Show only 2023 orders"* | Filtered analysis on any of the above |
| **Pure Question** | *"What columns are in this dataset?"* | Text answer, no chart |

---

## Project Structure

```
DataCopilot/
├── app.py                  # Flask application & API routes
├── copilot.py              # Mistral API integration and prompt templates
├── executor.py             # Sandboxed code execution engine
├── schema.py               # Dataset schema extraction
├── requirements.txt        # Python dependencies
├── .env                    # API key & model configuration (not committed)
├── sample_data.csv         # Example dataset for testing
├── templates/
│   └── index.html          # Single-page UI
├── static/
│   ├── css/style.css       # Application styling
│   └── js/app.js           # Frontend logic
├── uploads/                # Uploaded files (runtime, gitignored)
└── charts/                 # Generated chart images (runtime, gitignored)
```

---

## Security

- **Sandboxed Execution:** Generated code executes inside a restricted `exec()` sandbox with a limited set of safe built-ins.
- **Blocked Imports:** Imports such as `os`, `sys`, `subprocess`, and `shutil` are blocked, along with `open()`, `eval()`, `exec()`, and `compile()`.
- **Temporary Storage:** Uploaded files are stored temporarily in `uploads/` and should be cleared periodically in production.
- **API Key Protection:** The `.env` file must never be committed to version control.

### Production Recommendations

- Add user authentication
- Run behind a reverse proxy (e.g., nginx or Caddy)
- Configure HTTPS
- Implement rate limiting

---

## Troubleshooting

### `MISTRAL_API_KEY environment variable is not set`

Confirm the `.env` file exists in the same directory as `app.py`, with no spaces around `=` and no quotes around the value.

### `Mistral API error 401: Unauthorized`

Your API key is invalid, expired, or was copied incorrectly. Generate a new key at [console.mistral.ai/api-keys](https://console.mistral.ai/api-keys).

### Chart not appearing in chat

Check that the `charts/` folder exists and is writable. Verify the generated code includes `plt.savefig(chart_path, ...)`.

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue on the [GitHub repository](https://github.com/Pranish-Sapkota/DataCopilot).

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## License

This project is licensed under the **GNU General Public License v3.0**.

See the [LICENSE](LICENSE) file for full details.

---

<p align="center">
  Built with ❤️ by Pranish Sapkota using <a href="https://docs.mistral.ai/">Mistral AI</a> and <a href="https://flask.palletsprojects.com/">Flask</a>.
</p>
