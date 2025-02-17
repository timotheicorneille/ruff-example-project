# Ruff Example Project

This is an example Python project showcasing how to use **Ruff** for linting and formatting.

## 🛠 Setup

```bash
git clone https://github.com/yourusername/ruff-example-project.git
cd ruff-example-project
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
pre-commit install
```

## 🚀 Running the CLI

```bash
python src/main.py --name "Alice"
```

## 🧪 Running Tests

```bash
pytest
```

## 🔍 Running Linter

```bash
ruff check .
```

## 📜 Formatting Code

```bash
ruff format .
```
