
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask import Flask
from werkzeug.utils import secure_filename



class UploadForm(FlaskForm):
    description = TextAreaField('Image Description')
    photo = FileField('photo', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Appropriate Images Only')])