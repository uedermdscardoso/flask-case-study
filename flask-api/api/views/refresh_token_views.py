from datetime import timedelta

from flask import jsonify, make_response

from api import api
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, create_access_token, create_refresh_token, jwt_refresh_token_required

class RefreshTokenList(Resource):
    @jwt_refresh_token_required
    def post(self):
        usuario_token = get_jwt_identity()
        access_token = create_access_token(identity=usuario_token, expires_delta=timedelta(seconds=60))
        refresh_token = create_refresh_token(identity=usuario_token)
        return make_response(jsonify({
                'access_token': access_token,
                'refresh_token': refresh_token,
                'message': 'Login realizado com sucesso'
            }), 200)

api.add_resource(RefreshTokenList, '/token/refresh')