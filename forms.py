from wtforms import Form 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, IntegerField
from wtforms.fields import EmailField, TextAreaField, PasswordField
from wtforms import validators

class UserForm(Form):
    matricula = StringField('Matricula',[
        validators.DataRequired(message = 'La matricula es requerida')])
    nombre = StringField('Nombre')
    apeP = StringField('apeP')
    apeM = StringField('apeM')
    email = EmailField('email')
