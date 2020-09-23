#Como o Model tarefa está funcionando
from api import marshmallow
from api.models import tarefa_model
from marshmallow import fields

#Serializer
class TarefaSchema(marshmallow.Schema):
    class Meta:
        model = tarefa_model.Tarefa
        fields = ( 'id', 'titulo', 'descricao', 'data_expiracao', 'projeto', '_links' ) # projeto é chave estrangeira

    #Regras de validação
    titulo = fields.String(required=True)
    descricao = fields.String(required=True)
    data_expiracao = fields.Date(required=True)
    projeto = fields.String(required=True)

    #Implementando hateoas
    _links = marshmallow.Hyperlinks(
        {
            "get": marshmallow.URLFor("tarefadetail", id="<id>"),
            "post": marshmallow.URLFor("tarefadetail", id="<id>"),
            "delete": marshmallow.URLFor("tarefadetail", id="<id>")
        }
    )
