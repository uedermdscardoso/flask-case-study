from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from flask_babel import Babel

app = Flask(__name__) #Nome da aplicação que o arquivo init.py se encontrar

#database config
#USERNAME = 'root'
#PASSWORD = ''
#SERVER = 'localhost'
#DB_NAME = 'flask_db'

#app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB_NAME}'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config.from_object('config') #config.py

db = SQLAlchemy(app)
migrate = Migrate(app, db) #Criando uma instância
csrf = CSRFProtect(app)
csrf.init_app(app) #Iniciar a garantia de segurança do csrf

babel = Babel(app) #Utilizando babel na aplicação

#from .views import cliente_view #não refatorado
from .views import cliente_view_refact #refatorado
from .models import cliente_model

#Commands for flask migrate
#flask db init
#flask db migrate
#flask db upgrade