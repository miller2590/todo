from flask import Flask, render_template, redirect, url_for
from models.forms import AddTask, TaskOptions

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MY_LITTLE_SECRET'

objectives = {}


@app.route('/', methods=["GET", "POST"])
def index():
    todo_form = AddTask()
    new_id = len(objectives) + 1

    if todo_form.validate_on_submit():
        new_task = todo_form.todo.data
        objectives[new_id] = new_task
        return redirect(url_for("index"))

    return render_template('base.html', template_form=todo_form, objectives=objectives)


@app.route('/options/<int:id>', methods=["GET", "POST"])
def options(id):
    option_form = TaskOptions()

    if option_form.is_submitted():
        objectives.pop(id)
        return redirect(url_for('index'))

    return render_template('options.html', template_todo=objectives[id], template_form=option_form)


if __name__ == '__main__':
    app.run()
