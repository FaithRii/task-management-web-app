from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    priority = db.Column(db.String(20), nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    done = db.Column(db.Boolean, default=False)

@app.route('/')
def index():
    tasks = Task.query.order_by(Task.due_date).all()
    today = date.today()

    total = len(tasks)
    completed = sum(1 for t in tasks if t.done)
    overdue = sum(1 for t in tasks if not t.done and t.due_date < today)
    due_today = sum(1 for t in tasks if not t.done and t.due_date == today)

    stats = {
        'total': total,
        'completed': completed,
        'overdue': overdue,
        'due_today': due_today,
        'remaining': total - completed
    }

    return render_template('index.html', tasks=tasks, stats=stats, today=today)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form['title']
    description = request.form.get('description', '')
    priority = request.form['priority']
    due_date = datetime.strptime(request.form['due_date'], '%Y-%m-%d').date()

    new_task = Task(title=title, description=description, priority=priority, due_date=due_date)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/toggle/<int:id>')
def toggle_task(id):
    task = db.session.get(Task, id)
    if task:
        task.done = not task.done
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_task(id):
    task = db.session.get(Task, id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
    task = db.session.get(Task, id)
    if not task:
        return redirect(url_for('index'))
    if request.method == 'POST':
        task.title = request.form['title']
        task.description = request.form.get('description', '')
        task.priority = request.form['priority']
        task.due_date = datetime.strptime(request.form['due_date'], '%Y-%m-%d').date()
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', task=task)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
