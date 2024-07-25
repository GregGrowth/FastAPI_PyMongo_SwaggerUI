import os
from dotenv import load_dotenv
from urllib.parse import quote_plus
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Importer la config depuis le fichier .env
load_dotenv()
user = os.environ["USER"]
pwd = os.environ["PASSWORD"]
cluster = os.environ["CLUSTER"]
data_base_name = os.environ["DB_NAME"]
# collections_name = os.environ["COLL_NAME"]
# print(user)
# print(pwd)
# print(cluster)
# print(data_base_name)
# print(collections_name)

# Encoder le nom d'utilisateur et le mot de passe
user_encoded = quote_plus(user)
pwd_encoded = quote_plus(pwd)

# Consolidation de l'uri de connexion
uri = f"mongodb+srv://{user_encoded}:{pwd_encoded}@{cluster}.mongodb.net/"
print(uri)

# Creation d'une instance de la classe MongoManager
mongo_client = MongoClient(uri, server_api=ServerApi('1'), tls=True)
database = mongo_client.get_database("digischool")
