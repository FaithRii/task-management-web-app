# TaskFlow — Task Management Web App

A full-stack productivity web application built with **Python Flask**, **SQLAlchemy**, and **SQLite**. Features a modern dark dashboard UI with real-time task statistics, priority management, due date tracking, and overdue detection.

---

## 🖥️ Preview

> *(Add a screenshot or GIF here by dragging an image into this section on GitHub)*

---

## ✨ Features

- **Dashboard stats** — Live counters for Total, Completed, Remaining, Overdue, and Due Today
- **Add tasks** with title, description, priority, and due date
- **Edit tasks** — Update any task details at any time
- **Mark complete/incomplete** with a single click
- **Delete tasks** with confirmation prompt
- **Overdue detection** — Automatically flags tasks past their due date in red
- **Due today** — Highlights tasks due on the current date in yellow
- **Sidebar navigation** layout — Full screen dashboard design
- **Responsive** — Works on mobile and desktop

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Database | SQLite via SQLAlchemy ORM |
| Frontend | HTML5, CSS3, Jinja2 Templating |
| Deployment | Render (Gunicorn) |

---

## 🚀 Running Locally

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/taskflow.git
cd taskflow
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
python app.py
```

**4. Open in browser**
```
http://127.0.0.1:5000
```

---

## 📁 Project Structure

```
taskflow/
├── app.py                  # Flask routes and SQLAlchemy models
├── requirements.txt        # Python dependencies
├── Procfile                # Deployment config for Render
├── templates/
│   ├── index.html          # Main dashboard
│   └── edit.html           # Edit task page
└── static/
    └── style.css           # Stylesheet
```

---

## 🌐 Live Demo

> *(Add your Render deployment link here once deployed)*

---

## 👤 Author

**[Your Name]** — [github.com/yourusername](https://github.com/yourusername)
