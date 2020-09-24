import uuid

from flask_restful import Resource
from api import api
from ..schemas import usuario_schema
from flask import request, make_response, jsonify
from ..entidades import usuario
from ..services import usuario_service

class UsuarioList(Resource): #Métodos que não precisam de parâmetros
    def post(self):
        us = usuario_schema.UsuarioSchema()
        validate = us.validate(request.json) #Validar os dados recebidos

        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            email = request.json['email']
            senha = request.json['senha']
            is_admin = request.json['is_admin']
            api_key = str(uuid.uuid4())

            usuario_novo = usuario.Usuario(nome=nome, email=email, senha=senha, is_admin=is_admin, api_key=api_key)
            result = usuario_service.cadastrarUsuario(usuario_novo)

            return make_response(us.jsonify(result), 201)

api.add_resource(UsuarioList, '/usuarios') #Acessado pela rota 'usuarios'