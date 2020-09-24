from ..models import usuario_model
from api import db

def cadastrarUsuario(usuario):
    usuario_bd = usuario_model.Usuario(nome=usuario.nome, email=usuario.email, senha=usuario.senha, is_admin=usuario.is_admin, api_key=usuario.api_key)
    usuario_bd.gen_senha()
    db.session.add(usuario_bd)
    db.session.commit();
    return usuario_bd

def listarUsuarioPorEmail(email):
    return usuario_model.Usuario.query.filter_by(email=email).first()

def listarUsuarioPorId(id):
    return usuario_model.Usuario.query.filter_by(id=id).first()

def listarUsuarioPorApiKey(api_key):
    return usuario_model.Usuario.query.filter_by(api_key=api_key).first()