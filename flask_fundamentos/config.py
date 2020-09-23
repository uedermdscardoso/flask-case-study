#application config
DEBUG = True

#database config
USERNAME = 'root'
PASSWORD = ''
SERVER = 'localhost'
PORT = '3306'
DB_NAME = 'flask_db'
#SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}:{PORT}/{DB_NAME}'
SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}@{SERVER}:{PORT}/{DB_NAME}'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY='minha-chave-secreta' #Esse Hash irá identificar a aplicaçõ #CSRF
#Garante que a sua aplicação é que irá submetir o formulário

BABEL_DEFAULT_LOCALE = 'pt'