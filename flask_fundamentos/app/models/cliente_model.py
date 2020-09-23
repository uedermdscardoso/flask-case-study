from app import db  #importando a instância db
from sqlalchemy_utils import ChoiceType #package SQLAlchemy-Utis

class Cliente(db.Model):
    __tablename__ = 'clientes'

    GENERO_CHOICES = [
        (u'M', u'Masculino'),
        (u'F', u'Feminino'),
        (u'N', u'Nenhuma das opções')
    ]

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(200), unique=True)
    data_nascimento = db.Column(db.DateTime())
    profissao = db.Column(db.String(30))
    genero = db.Column(ChoiceType(GENERO_CHOICES))