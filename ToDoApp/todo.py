from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

# Database Ayarları
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "todo.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Todo Modeli
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    complete = db.Column(db.Boolean, default=False)
    
    priority = db.Column(db.Integer, default=1)  # Öncelik Durumu
    category = db.Column(db.String(50), default="Genel") # Kategori
    due_date = db.Column(db.Date, nullable=True) # Son tarih

@app.route("/")
def index():
    # Arama Sorgusu
    q = request.args.get("q")
    
    query = Todo.query

    # Eğer arama yapılmışsa filtrele
    if q:
        query = query.filter(Todo.title.contains(q))

    # Aktif olmayanlar önce, sonra öncelik ve tarih sıralaması
    todos = query.order_by(Todo.complete, Todo.priority.desc(), Todo.due_date).all()
    
    return render_template("index.html", todos=todos, today=datetime.today().date())

@app.route("/add", methods=["POST"])
def addTodo():
    title = request.form.get("title")
    priority = int(request.form.get("priority"))
    category = request.form.get("category")
    date_str = request.form.get("due_date")

    if not title or title.strip() == "":
        return redirect(url_for("index"))

    # Tarih seçildiyse Python tarih formatına çevir, seçilmediyse None yap
    due_date_obj = datetime.strptime(date_str, '%Y-%m-%d').date() if date_str else None

    newTodo = Todo(title=title, priority=priority, category=category, due_date=due_date_obj)
    db.session.add(newTodo)
    db.session.commit()
    return redirect(url_for("index"))

# Düzenleme sayfası ve işlemi
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def editTodo(id):
    todo = Todo.query.get_or_404(id)
    
    if request.method == "POST":
        todo.title = request.form.get("title")
        todo.priority = int(request.form.get("priority"))
        todo.category = request.form.get("category")
        date_str = request.form.get("due_date")
        todo.due_date = datetime.strptime(date_str, '%Y-%m-%d').date() if date_str else None
        
        db.session.commit()
        return redirect(url_for("index"))
        
    return render_template("edit.html", todo=todo)

@app.route("/toggle/<int:id>")
def toggleTodo(id):
    todo = Todo.query.get_or_404(id)
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<int:id>")
def deleteTodo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)