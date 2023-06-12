from pymongo import MongoClient
from dotenv import dotenv_values
import certifi

config = dotenv_values('.env')
ca = certifi.where()

MONGO_URL = config['MONGO_URI']
#Funcion para conectarse a mongo con los paquetes instalados 
def conection_db():
    try:
        client = MongoClient(MONGO_URL, tlsCAFile = ca)
        db = client['VillaNueva']
    except ConnectionError:
        print('Error al  conectarse')
    return db