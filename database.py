'''from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://manzanaresdionicio:arleys1234@cluster0.2tfkn8g.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient.connect(MONGO_URI, tlsCAFile=ca)
        db=client=["villanueva"]
    except ConnectionError:
        print("Error de conexión con la BDD")
    return db'''
