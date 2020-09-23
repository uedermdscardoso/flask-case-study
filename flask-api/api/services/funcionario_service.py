from ..models import funcionario_model
from api import db

def listarFuncionarios():
    funcionarios = funcionario_model.Funcionario.query.all()
    return funcionarios

def listarFuncionario(id):
    funcionario = funcionario_model.Funcionario.query.filter_by(id=id).first()
    return funcionario

def cadastrarFuncionario(funcionario):
    funcionario_bd = funcionario_model.Funcionario(nome=funcionario.nome, idade=funcionario.idade)
    db.session.add(funcionario_bd)
    db.session.commit();
    return funcionario_bd

def editarFuncionario(funcionario_bd, funcionario_novo):
    funcionario_bd.nome = funcionario_novo.nome
    funcionario_bd.idade = funcionario_novo.idade
    db.session.commit()

def removerFuncionario(funcionario):
    db.session.delete(funcionario)
    db.session.commit()
