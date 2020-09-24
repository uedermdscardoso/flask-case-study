from api import api, jwt
from flask_restful import Resource
from ..schemas.login_schema import LoginSchema
from ..services import usuario_service
from flask import request, make_response, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import timedelta

class LoginList(Resource):

    @jwt.user_claims_loader
    def add_claims_to_access_token(identity):
        usuario_token = usuario_service.listarUsuarioPorId(identity)
        if usuario_token.is_admin:
            roles = 'admin'
        else:
            roles = 'user'
        return { 'roles': roles }

    def post(self):
        ls = LoginSchema()
        validate = ls.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        email = request.json['email']
        senha = request.json['senha']
        usuario_bd = usuario_service.listarUsuarioPorEmail(email)
        if usuario_bd and usuario_bd.ver_senha(senha):
            access_token = create_access_token(identity=usuario_bd.id, expires_delta=timedelta(seconds=60))
            refresh_token = create_refresh_token(identity=usuario_bd.id)
            return make_response(jsonify({
                'access_token': access_token,
                'refresh_token': refresh_token,
                'message': 'Login realizado com sucesso'
            }), 200)
        return make_response(jsonify({
            'message': 'Credenciais inválidas'
        }), 401)

api.add_resource(LoginList, '/login')
