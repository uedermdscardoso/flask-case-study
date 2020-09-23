from app.models import cliente_model
from app import db

def listarClientes():
    clientes = cliente_model.Cliente.query.all()
    return clientes

def listarClientePorId(id):
    cliente = cliente_model.Cliente.query.filter_by(id=id).first()
    return cliente

def cadastrarCliente(cliente):
    db.session.add(cliente)
    db.session.commit()

def editarCliente(cliente_bd, cliente_novo):
    cliente_bd.nome = cliente_novo.nome
    cliente_bd.email = cliente_novo.email
    cliente_bd.data_nascimento = cliente_novo.data_nascimento
    cliente_bd.profissao = cliente_novo.profissao
    cliente_bd.genero = cliente_novo.genero
    db.session.commit()

def removerCliente(cliente):
    db.session.delete(cliente)
    db.session.commit()
