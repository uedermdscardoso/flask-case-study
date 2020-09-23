#coordena o projeto

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flasgger import Swagger

app = Flask(__name__)
app.config.from_object('config') #config.py
db = SQLAlchemy(app)
marshmallow = Marshmallow(app)
migrate = Migrate(app, db) #Criando uma instância
JWTManager(app) #Para gerar novos jsons webtokens

api = Api(app)
swagger = Swagger(app)

from .views import tarefa_views, projeto_views, funcionario_views, usuario_views, login_views #Para fucar acessível na aplicação
from .models import tarefa_model, projeto_model, funcionario_model, usuario_model

#Commands for flask migrate
#export FLASK_APP=api.py  ou  set FLASK_APP=api.py
#flask db init
#flask db migrate
#flask db upgrade


#Swagger
#http://127.0.0.1:5000/apidocs/