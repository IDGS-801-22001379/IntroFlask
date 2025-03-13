from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField, RadioField
from wtforms.validators import DataRequired, Email, Length, NumberRange

from wtforms.validators import DataRequired, Length, NumberRange

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




class ZodiacoForm(FlaskForm):
    nombre = StringField("Nombre", [
        DataRequired(message="El campo es requerido."),
        Length(min=2, max=50, message="Debe tener entre 2 y 50 caracteres.")
    ])
    
    apellido_paterno = StringField("Apellido Paterno", [
        DataRequired(message="El campo es requerido.")
    ])
    
    apellido_materno = StringField("Apellido Materno", [
        DataRequired(message="El campo es requerido.")
    ])
    
    dia = IntegerField("Día de Nacimiento", [
        DataRequired(message="El campo es requerido."),
        NumberRange(min=1, max=31, message="Día inválido.")
    ])
    
    mes = IntegerField("Mes de Nacimiento", [
        DataRequired(message="El campo es requerido."),
        NumberRange(min=1, max=12, message="Mes inválido.")
    ])
    
    anio = IntegerField("Año de Nacimiento", [
        DataRequired(message="El campo es requerido."),
        NumberRange(min=1900, max=2100, message="Año inválido.")
    ])
    
    sexo = RadioField("Sexo", choices=[("M", "Masculino"), ("F", "Femenino")], validators=[DataRequired()])








class CinepolisForm(FlaskForm):
    nombre = StringField("Nombre", [
        DataRequired(message="El campo es requerido.")
    ])

    cantidad_compradores = IntegerField("Cantidad de Compradores", [
        DataRequired(message="El campo es requerido."),
        NumberRange(min=1, message="Debe haber al menos un comprador.")
    ])

    cantidad_boletos = IntegerField("Cantidad de Boletos", [
        DataRequired(message="El campo es requerido."),
        NumberRange(min=1, message="Debe comprar al menos un boleto.")
    ])

    tarjeta = RadioField("Tarjeta Cineco", choices=[
        ("si", "Sí"),
        ("no", "No")
    ], validators=[DataRequired(message="Seleccione una opción.")])
