#Como o Model tarefa está funcionando
from api import marshmallow
from api.models import projeto_model
from marshmallow import fields

#Serializer
class ProjetoSchema(marshmallow.ModelSchema):
    class Meta:
        model = projeto_model.Projeto
        fields = ( 'id', 'nome', 'descricao', 'tarefas', 'funcionarios' ) #tarefas e funcionarios são relacionamentos

    #Regras de validação
    nome = fields.String(required=True)
    descricao = fields.String(required=True)