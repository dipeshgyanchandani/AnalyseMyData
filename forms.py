from flask_wtf import FlaskForm
from wtforms import FileField, TextAreaField


class UploadForm(FlaskForm):
    description  = TextAreaField('Image Description')
    file__ = FileField('Image File')

    def validate_image(self):
        if self.file__.data:
            print("This is my file...",self.file__.data )
