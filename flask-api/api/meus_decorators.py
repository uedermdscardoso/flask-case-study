from functools import wraps

from flask import jsonify, make_response, request
from flask_jwt_extended import verify_jwt_in_request, get_jwt_claims
from .services import usuario_service

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request() #Se existe token na requisição
        claims = get_jwt_claims()
        if claims['roles'] != 'admin':
            return make_response(jsonify(mensagem='Não permitido'), 403)
        else:
            return fn(*args, *kwargs)
    return wrapper

def api_key_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        api_key = request.args.get('api_key')  #passando um parâmetro api_key pelo postman
        if api_key and usuario_service.listarUsuarioPorApiKey(api_key):
            return fn(*args, *kwargs) #Requisição continue
        else:
            return make_response(jsonify(mensagem='Não autorizado'), 401)
    return wrapper