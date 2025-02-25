from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField
from wtforms.validators import DataRequired, Email, Length

class UserForm(FlaskForm):
    matricula = StringField("Matrícula", [
        DataRequired(message="El campo es requerido."),
        Length(min=3, max=10, message="Debe tener entre 3 y 10 caracteres.") 
    ])
    
    nombre = StringField("Nombre", [
        DataRequired(message="El campo es requerido.")
    ])

    apellido = StringField("Apellido", [
        DataRequired(message="El campo es requerido.")
    ])

    correo = EmailField("Correo", [
    DataRequired(message="El campo es requerido."),
    Email(message="Debe ser un correo válido.")  
    ])


