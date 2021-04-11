from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask import Flask
from werkzeug.utils import secure_filename
from wtforms import TextAreaField, StringField
from wtforms.validators import DataRequired


class UploadForm(FlaskForm):
    description = StringField('Description', validators=[DataRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')])