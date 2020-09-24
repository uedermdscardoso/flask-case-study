from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_claims
from api import api
from ..schemas import tarefa_schema
from flask import request, make_response, jsonify
from ..entidades import tarefa
from ..services import tarefa_service, projeto_service
from ..pagination import paginate
from ..models.tarefa_model import Tarefa
from ..meus_decorators import admin_required, api_key_required

class TarefaList(Resource): #Métodos que não precisam de parâmetros

    #@jwt_required  #Precisda de autenticação
    @api_key_required
    def get(self):
        #tarefas = tarefa_service.listarTarefas()
        ts = tarefa_schema.TarefaSchema(many=True) #many = True para deserializar mais que um objeto
        #return make_response(ts.jsonify(tarefas), 200)
        return paginate(Tarefa, ts) #aplicando paginação

    #@jwt_required
    @admin_required
    def post(self):
        #claims = get_jwt_claims()  # Verificação de perfil de acesso - substituído pelo arquivo meus_decorators
        #if claims['roles'] != 'admin':
        #    return make_response(jsonify(mensagem='Não permitido'), 403)

        ts = tarefa_schema.TarefaSchema()
        validate = ts.validate(request.json) #Validar os dados recebidos
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            titulo = request.json['titulo']
            descricao = request.json['descricao']
            data_expiracao = request.json['data_expiracao']
            projeto = request.json['projeto']

            projeto_tarefa = projeto_service.listarProjeto(projeto)
            if projeto_tarefa is None:
                return make_response(jsonify('Projeto não encontrado'), 404)

            tarefa_nova = tarefa.Tarefa(titulo=titulo, descricao=descricao, data_expiracao=data_expiracao, projeto=projeto_tarefa)
            result = tarefa_service.cadastrarTarefa(tarefa_nova)

            return make_response(ts.jsonify(result), 201)

class TarefaDetail(Resource): #Métodos que precisam de parâmetros
    def get(self, id):
        tarefa = tarefa_service.listarTarefa(id)
        if tarefa is None: #Não existe no banco de dados
            return make_response(jsonify('Tarefa não encontrada'), 404)
        ts = tarefa_schema.TarefaSchema()
        return make_response(ts.jsonify(tarefa), 200)

    def put(self, id):
        tarefa_bd = tarefa_service.listarTarefa(id)
        if tarefa_bd is None:
            return make_response(jsonify('Tarefa não encontrada'), 404)
        ts = tarefa_schema.TarefaSchema()
        validate = ts.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            titulo = request.json['titulo']
            descricao = request.json['descricao']
            data_expiracao = request.json['data_expiracao']
            projeto = request.json['projeto']

            projeto_tarefa = projeto_service.listarProjeto(projeto)
            if projeto_tarefa is None:
                return make_response(jsonify('Projeto não encontrado'), 404)

            tarefa_nova = tarefa.Tarefa(titulo=titulo, descricao=descricao, data_expiracao=data_expiracao, projeto=projeto_tarefa)

            tarefa_service.editarTarefa(tarefa_bd,tarefa_nova)
            tarefa_atualizada = tarefa_service.listarTarefa(id)

            return make_response(ts.jsonify(tarefa_atualizada),200)

    def delete(self, id):
        tarefa = tarefa_service.listarTarefa(id)
        if tarefa is None:
            return make_response(jsonify('Tarefa não encontrada'), 400)
        tarefa_service.removerTarefa(tarefa)
        return make_response('', 204)

api.add_resource(TarefaList, '/tarefas') #Acessado pela rota 'tarefas'
api.add_resource(TarefaDetail, '/tarefas/<int:id>')