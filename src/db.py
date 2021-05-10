import pymongo as pymongo
from dotenv import dotenv_values

config = dotenv_values(".env")


        
def connectDB(collectionName):
    client = pymongo.MongoClient("mongodb+srv://{}:{}@cluster0.79bpm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority".format(config['MONGO_USER'], config['MONGO_PSWD']))

    db = client["VideoGameReccomender"]
    collection = db[collectionName]
    
    
    return collection

