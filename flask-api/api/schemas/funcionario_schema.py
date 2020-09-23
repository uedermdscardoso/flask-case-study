#Como o Model tarefa está funcionando
from api import marshmallow
from api.models import funcionario_model
from marshmallow import fields

#Serializer
class FuncionarioSchema(marshmallow.ModelSchema):
    class Meta:
        model = funcionario_model.Funcionario
        fields = ( 'id', 'nome', 'idade', 'projetos' ) #projetos é derivado de relacionamento

    #Regras de validação
    nome = fields.String(required=True)
    idade = fields.Integer(required=True)