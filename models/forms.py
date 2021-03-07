from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddTask(FlaskForm):
    todo = StringField("Todo", validators=[DataRequired()])
    submit = SubmitField("Add Daunting Task")


class TaskOptions(FlaskForm):
    delete = SubmitField("Delete Task")
