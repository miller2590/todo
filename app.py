import environ as environ
from flask import Flask, render_template, redirect, url_for
from models.forms import AddTask, TaskOptions
from os import environ


app = Flask(__name__)
app.config['SECRET_KEY'] = 'MY_LITTLE_SECRET'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL') or 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from models.tables import Task, db


@app.route('/', methods=["GET", "POST"])
def index():
    todo_form = AddTask()

    if todo_form.validate_on_submit():
        new_task = Task(title=todo_form.todo.data)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for("index"))

    return render_template('base.html', template_form=todo_form, todos=Task.query.all())


@app.route('/options/<int:id>', methods=["GET", "POST"])
def options(id):
    delete_form = TaskOptions()
    current_task = Task.query.get(id)

    if delete_form.is_submitted():
        db.session.delete(current_task)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('options.html', template_form=delete_form, task=current_task.title)


if __name__ == '__main__':
    app.run()
