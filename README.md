# 📊 DataCopilot

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/backend-Flask-000000.svg?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![AI Integration](https://img.shields.io/badge/AI-Anthropic%20Claude-CC9900.svg)](https://www.anthropic.com/)
[![License](https://img.shields.io/badge/License-GPL--3.0-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.html)

# <span style="color: #db7226;">&lt;DataCopilot/&gt;</span>

**DataCopilot** is an intelligent, web-based data assistant that lets you interact with your datasets using natural language. Powered by Anthropic's Claude API, it translates plain-English questions into Python or Pandas code, executes it in a secure sandboxed environment, and returns the results—all through a clean, single-page web interface.

Whether you're exploring a CSV, cleaning messy data, or generating quick statistics, DataCopilot acts as your copilot for data analysis.

## ✨ Features

- **Natural Language Querying** – Ask questions in plain English and get answers from your data.
- **AI-Powered Code Generation** – Uses Anthropic Claude to generate accurate Python/Pandas code.
- **Safe Code Execution** – Runs all generated code in an isolated, sandboxed environment to protect your system.
- **Interactive Web UI** – Clean, responsive single-page interface built with Flask, HTML, CSS, and JavaScript.
- **Dynamic Schema Understanding** – Automatically builds and understands your DataFrame structure for precise query handling.

## 🧰 Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python 3, Flask |
| AI Integration | Anthropic Claude API |
| Data Processing | Pandas |
| Code Execution | Sandboxed Python runner |
| Frontend | HTML, CSS, JavaScript |
| License | GPL-3.0 |

## 📁 Project Structure

```
datacopilot/
├── app.py            # Flask entry point & routes
├── copilot.py        # Anthropic API integration & prompt logic
├── executor.py       # Safe sandboxed code runner
├── schema.py         # DataFrame schema builder
├── requirements.txt  # Python dependencies
├── templates/
│   └── index.html    # Single-page UI
└── static/
    ├── css/style.css
    └── js/app.js
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- An [Anthropic API key](https://console.anthropic.com/)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Pranish-Sapkota/DataCopilot.git
   cd DataCopilot
   ```

2. **Create and activate a virtual environment** (recommended)

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your Anthropic API key**

   Create a `.env` file in the project root or set an environment variable:

   ```bash
   export ANTHROPIC_API_KEY="your-api-key-here"
   ```

   Or add it to a `.env` file:

   ```
   ANTHROPIC_API_KEY=your-api-key-here
   ```

### Running the Application

```bash
python app.py
```

Then open your browser and navigate to **http://localhost:5000**.

## 🧪 Usage

1. Upload or load your dataset (CSV format supported).
2. Type a question in natural language — for example:
   - *"What are the average values of each numeric column?"*
   - *"Show me the top 10 rows sorted by column X."*
   - *"How many missing values are in each column?"*
3. DataCopilot generates the corresponding Python/Pandas code.
4. The code is executed safely, and the results are displayed in the UI.

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository** and create your branch from `main`.
2. **Make your changes** – whether it's a bug fix, new feature, or documentation improvement.
3. **Test your changes** thoroughly.
4. **Submit a pull request** with a clear description of what you've done.

Please make sure to update the README or documentation accordingly if your changes introduce new behavior.

## 🐛 Reporting Issues

Found a bug or have a suggestion? Please [open an issue](https://github.com/Pranish-Sapkota/DataCopilot/issues) with the following information:

- A clear and descriptive title.
- Steps to reproduce the issue.
- Expected vs. actual behavior.
- Screenshots or code snippets if applicable.
- Your environment (OS, Python version, browser, etc.).

## 📄 License

This project is licensed under the **GNU General Public License v3.0**. See the [LICENSE](LICENSE) file for the full text.

## 🙏 Acknowledgements

- [Anthropic](https://www.anthropic.com/) for providing the Claude API.
- [Pandas](https://pandas.pydata.org/) for data manipulation.
- [Flask](https://flask.palletsprojects.com/) for the lightweight web framework.

---

**Built with ❤️ by [Pranish Sapkota](https://github.com/Pranish-Sapkota)**

    ├── css/style.css # Custom dashboard layout and theme styling
    └── js/app.js     # Frontend state handler and API connector
