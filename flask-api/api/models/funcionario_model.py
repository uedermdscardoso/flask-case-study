from api import db  #importando a instância db

class Funcionario(db.Model):
    __tablename__ = 'funcionario'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    idade = db.Column(db.Integer, nullable=False)

    #Relacionamento de n para n
    projetos = db.relationship('Projeto', secondary='funcionario_projeto', back_populates='funcionarios')