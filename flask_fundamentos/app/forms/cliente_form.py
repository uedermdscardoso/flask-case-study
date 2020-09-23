#Determina regras de validação do formulário cliente
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.fields.html5 import EmailField, DateField
from wtforms.validators import DataRequired, Email

class ClienteForm(FlaskForm):
    nome = StringField('nome', validators=[ DataRequired() ])
    email = EmailField('email', validators=[Email(), DataRequired()])
    data_nascimento = DateField('data_nascimento', validators=[DataRequired()], format='%Y-%m-%d')
    profissao = StringField('profissao', validators=[DataRequired()])
    genero = SelectField('genero', validators=[DataRequired()], choices=[('F','Feminino'),('M','Masculino'),('N','Nenhuma das opções')])