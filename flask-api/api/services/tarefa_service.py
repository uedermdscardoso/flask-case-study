from ..models import tarefa_model
from api import db

def listarTarefas():
    tarefas = tarefa_model.Tarefa.query.all()
    return tarefas

def listarTarefa(id):
    tarefa = tarefa_model.Tarefa.query.filter_by(id=id).first()
    return tarefa

def cadastrarTarefa(tarefa):
    tarefa_bd = tarefa_model.Tarefa(titulo=tarefa.titulo, descricao=tarefa.descricao, data_expiracao=tarefa.data_expiracao, projeto=tarefa.projeto)
    db.session.add(tarefa_bd)
    db.session.commit();
    return tarefa_bd

def editarTarefa(tarefa_bd, tarefa_novo):
    tarefa_bd.titulo = tarefa_novo.titulo
    tarefa_bd.descricao = tarefa_novo.descricao
    tarefa_bd.data_expiracao = tarefa_novo.data_expiracao
    tarefa_bd.projeto = tarefa_novo.projeto
    db.session.commit()

def removerTarefa(tarefa):
    db.session.delete(tarefa)
    db.session.commit()
