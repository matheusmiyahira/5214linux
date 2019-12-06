from pymongo import MongoClient

#Fazer conexão
mongo_con = MongoClient()
#Usar Banco
db = mongo_con['flask-app']