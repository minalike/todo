from flask import Flask, render_template, redirect, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

    
@app.route("/")
def index():
    # show all todos
    todo_list =Todo.query.all()
    return render_template("base.html", todo_list=todo_list)


@app.route("/add", methods=["POST"])
def add():
    """Add a to-do item and commit to database."""
    task_name = request.form.get("title")
    new_task = Todo(title=task_name, complete=False)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/about")
def about():
    return "About"


if __name__ == "__main__":
    db.create_all()

    app.run(debug=True)