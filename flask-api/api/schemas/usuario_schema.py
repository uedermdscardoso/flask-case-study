#Como o Model tarefa está funcionando
from api import marshmallow
from api.models import usuario_model
from marshmallow import fields

#Serializer
class UsuarioSchema(marshmallow.ModelSchema):
    class Meta:
        model = usuario_model.Usuario
        fields = ( 'id', 'nome', 'email', 'senha', 'is_admin', 'api_key' )

    #Regras de validação
    nome = fields.String(required=True)
    email = fields.String(required=True)
    senha = fields.String(required=True)
    is_admin = fields.Boolean(required=True)
    api_key = fields.String(required=False)