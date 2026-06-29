# 📊 DataCopilot

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/backend-Flask-000000.svg?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![AI Integration](https://img.shields.io/badge/AI-Anthropic%20Claude-CC9900.svg)](https://www.anthropic.com/)
[![License](https://img.shields.io/badge/License-GPL--3.0-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.html)

<img width="900" src="data:image/jpeg;base64,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" alt="Logo"/>

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
