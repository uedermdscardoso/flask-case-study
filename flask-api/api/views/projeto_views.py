from flask_restful import Resource
from api import api
from ..schemas import projeto_schema
from flask import request, make_response, jsonify
from ..entidades import projeto
from ..services import projeto_service

class ProjetoList(Resource): #Métodos que não precisam de parâmetros
    def get(self):
        projetos = projeto_service.listarProjetos()
        ps = projeto_schema.ProjetoSchema(many=True) #many = True para deserializar mais que um objeto
        return make_response(ps.jsonify(projetos), 200)

    def post(self):
        ps = projeto_schema.ProjetoSchema()
        validate = ps.validate(request.json) #Validar os dados recebidos
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            descricao = request.json['descricao']
            funcionarios = request.json['funcionarios'] #ids

            projeto_novo = projeto.Projeto(nome=nome, descricao=descricao, funcionarios=funcionarios)
            result = projeto_service.cadastrarProjeto(projeto_novo)

            return make_response(ps.jsonify(result), 201)

class ProjetoDetail(Resource): #Métodos que precisam de parâmetros
    def get(self, id):
        projeto = projeto_service.listarProjeto(id)
        if projeto is None: #Não existe no banco de dados
            return make_response(jsonify('Projeto não encontrado'), 404)
        ps = projeto_schema.ProjetoSchema()
        return make_response(ps.jsonify(projeto), 200)

    def put(self, id):
        projeto_bd = projeto_service.listarProjeto(id)
        if projeto_bd is None:
            return make_response(jsonify('Projeto não encontrado'), 404)
        ps = projeto_schema.ProjetoSchema()
        validate = ps.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            descricao = request.json['descricao']
            funcionarios = request.json['funcionarios']  # ids

            projeto_novo = projeto.Projeto(nome=nome, descricao=descricao, funcionarios=funcionarios)
            projeto_service.editarProjeto(projeto_bd,projeto_novo)
            projeto_atualizado = projeto_service.listarProjeto(id)

            return make_response(ps.jsonify(projeto_atualizado),200)

    def delete(self, id):
        projeto = projeto_service.listarProjeto(id)
        if projeto is None:
            return make_response(jsonify('Projeto não encontrado'), 400)
        projeto_service.removerProjeto(projeto)
        return make_response('', 204)

api.add_resource(ProjetoList, '/projetos') #Acessado pela rota 'projetos'
api.add_resource(ProjetoDetail, '/projetos/<int:id>')