
# Code Versioning and Execution Platform

A web-based Python code editor built with Flask that allows users to write, run, save, and manage versions of their code. This is ideal for students, developers, or anyone needing a simple code versioning system.

## Features

- ✏️ Live Python code editor
- ▶️ Execute code directly in the browser (backend execution with subprocess)
- 📂 Save versions with custom filenames (prompted via dialog)
- ↩️ Load and delete previous versions
- 🌐 Simple web interface (HTML, CSS, JavaScript)
- ✨ Version listing with timestamps
- 🔐 Sign In / Sign Up Authentication *(Work in progress)*
- 🎨 UI/UX Enhancements *(Ongoing)*

## Tech Stack

- Python 3
- Flask
- SQLite (via SQLAlchemy)
- HTML/CSS/JavaScript

## How to Run the Project

1. **Clone the repository**
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. **Set up a virtual environment (optional but recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scriptsctivate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the Flask app**
```bash
python app.py
```

5. **Open in your browser**
```
http://localhost:5000/
```

## Folder Structure

```
project/
├── templates/
│   ├── editor.html
│   ├── versions.html
├── static/
│   ├── version.css
│   ├── script.js
├── app.py
├── requirements.txt
├── codes.db  # Auto-created on first run
├── README.md
```

## Authors
- Built by RAJMANI SHARMA ✨
