from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from typing import List # utilisation dans la fonction creat_many()

class MongoManager:
    # Creation du constructeur
    def __init__(self, uri: str, db_name: str, coll_name: str):
        self.__client = MongoClient(uri, server_api=ServerApi('1'), tls=True)       # attribut pour acceder ao moteir de la base de donnees mongo
        self.__db = self.__client.get_database(db_name)                             # attribut pour acceder a la base de donnees
        # Autre maniere : self.__db = self.__client[db_name]
        self.__collections = self.__db.get_collection(coll_name)                    # attribut pour acceder a la collection
        # Autre maniere : self.__collections = self.__db[coll_name]

    # Creation des getter et setter pour l'attribut __client
    @property
    def client(self):
        return self.__client
    @client.setter
    def client(self, new_uri_client):
        self.__client = MongoClient(new_uri_client, server_api=ServerApi('1'), tls=True)

    # Creation des getter et setter pour l'attribut __db
    @property
    def db(self):
        return self.__db
    @db.setter
    def db(self, db_name):
        self.__db = self.__client.get_database(db_name)
        # réaffectation obligatoire de la collection car changement de database
        self.collections = self.__collections.name  # .name car collection est un objet

    # Creation des getter et setter pour l'attribut __collections
    @property
    def collections(self):
        return self.__collections
    @collections.setter
    def collections(self, col_name):
        self.__collections = self.__db.get_collection(col_name)

    # Creation des fonctions permettant d'afficher les bases de donnees et les collections
    def list_databases(self):
        return self.__client.list_database_names()

    def list_collections(self):
        return self.__db.list_collection_names()

    # Creation des fonctions permettant d'inserer un ou plusieurs itemument
    def creat_one(self, item: dict):
        return self.__collections.insert_one(item)

    def creat_many(self, item: List[dict]):
        return self.__collections.insert_many(item)

    # Creation des fonctions permettant d'afficher un ou plusieurs itemument
    def read_one(self, filter: dict ={}, proj: dict ={}):
        return self.__collections.find_one(filter, proj)

    def read_many(self, filter: dict ={}, proj: dict ={}):
        try:
            return list(self.__collections.find(filter, proj))
        except Exception as e:
            print(e)

    # Creation des fonctions permettant de mettre a jour un ou plusieurs elements dans le itemument
    def update_one(self, filter, newValue):
        return self.__collections.update_one(filter, newValue)

    def update_many(self, filter, newValue):
        return self.__collections.update_many(filter, newValue)

    # Creation des fonctions permettant de supprimer un ou plusieurs elements dans le itemument
    def delete_one(self, filter):
        return self.__collections.delete_one(filter)

    def delete_many(self, filter):
        return self.__collections.delete_many(filter)

    # Fonction pour fermer la connection ! Bonne pratique
    def close_connection(self):
        self.__client.close()
        print("Fermeture de la connexion à MongoDB")
