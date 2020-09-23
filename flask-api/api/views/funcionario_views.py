from flask_restful import Resource
from api import api
from ..schemas import funcionario_schema
from flask import request, make_response, jsonify
from ..entidades import funcionario
from ..services import funcionario_service

class FuncionarioList(Resource): #Métodos que não precisam de parâmetros
    def get(self):
        funcionarios = funcionario_service.listarFuncionarios()
        fs = funcionario_schema.FuncionarioSchema(many=True) #many = True para deserializar mais que um objeto
        return make_response(fs.jsonify(funcionarios), 200)

    def post(self):
        fs = funcionario_schema.FuncionarioSchema()
        validate = fs.validate(request.json) #Validar os dados recebidos
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            idade = request.json['idade']

            funcionario_novo = funcionario.Funcionario(nome=nome, idade=idade)
            result = funcionario_service.cadastrarFuncionario(funcionario_novo)

            return make_response(fs.jsonify(result), 201)

class FuncionarioDetail(Resource): #Métodos que precisam de parâmetros
    def get(self, id):
        funcionario = funcionario_service.listarFuncionario(id)
        if funcionario is None: #Não existe no banco de dados
            return make_response(jsonify('Funcionário não encontrado'), 404)
        fs = funcionario_schema.FuncionarioSchema()
        return make_response(fs.jsonify(funcionario), 200)

    def put(self, id):
        funcionario_bd = funcionario_service.listarFuncionario(id)
        if funcionario_bd is None:
            return make_response(jsonify('Funcionário não encontrado'), 404)
        fs = funcionario_schema.FuncionarioSchema()
        validate = fs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            idade = request.json['idade']

            funcionario_novo = funcionario.Funcionario(nome=nome, idade=idade)
            funcionario_service.editarFuncionario(funcionario_bd,funcionario_novo)

            funcionario_atualizado = funcionario_service.listarFuncionario(id)

            return make_response(fs.jsonify(funcionario_atualizado),200)

    def delete(self, id):
        funcionario = funcionario_service.listarFuncionario(id)
        if funcionario is None:
            return make_response(jsonify('Funcionário não encontrado'), 400)
        funcionario_service.removerFuncionario(funcionario)
        return make_response('', 204)

api.add_resource(FuncionarioList, '/funcionarios') #Acessado pela rota 'projetos'
api.add_resource(FuncionarioDetail, '/funcionarios/<int:id>')