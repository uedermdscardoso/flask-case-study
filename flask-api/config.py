#application config
DEBUG = True

#database config
USERNAME = 'root'
PASSWORD = ''
SERVER = 'localhost'
PORT = '3306'
DB_NAME = 'flask_api'
#SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}:{PORT}/{DB_NAME}'
SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}@{SERVER}:{PORT}/{DB_NAME}'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'sua-aplicacao' #Identificação única