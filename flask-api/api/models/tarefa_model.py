from api import db  #importando a instância db

class Tarefa(db.Model):
    __tablename__ = 'tarefa'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    data_expiracao = db.Column(db.Date, nullable=False)

    #Relacionamento de 1 para n
    projeto_id = db.Column(db.Integer, db.ForeignKey('projeto.id'))
    projeto = db.relationship('Projeto', backref=db.backref('tarefas', lazy='dynamic')) #projeto_model.Projeto