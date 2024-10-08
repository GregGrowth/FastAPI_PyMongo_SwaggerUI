from db import database
from bson import ObjectId

# Selectionner la base de donnees (BDD)
collection = database["eleve"]

# Fonction permettant d'afficher un element de la BDD
def get_one(id: str):
    results = collection.find_one({"_id": ObjectId(id)}, {"_id": 0})
    return results

# Fontion permettant d'afficher les eleves selon le chois d'une classe
def get_eleve_choose_classe(id :str):
    results = collection.find({"classe": id}, {"_id": 0})
    return list(results)

# Fonction permettant d'afficher plusieurs elements de la BDD
def get_all():
    results = collection.find({}, {"_id": 0})
    return list(results)

# Fonction permettant d'inserer un element de la BDD
def create_one(item: dict):
    results = collection.insert_one(item)
    return results

# Fonction permettant d'inserer plusieurs elements de la BDD
def create_many(item):
    results = collection.insert_many(item)
    return results

# Fonction permettant de mettre a jour la classe d'un eleve de la BDD
def update_one(id_eleve: str, update: dict):
    results = collection.update_one({"id": id_eleve}, {"$set": update})
    return results

# Fonction permettant de mettre a jour plusieurs elements de la BDD
def update_many(filter, newValue):
    results = collection.update_many(filter, newValue)
    return results

# Fonction permettant de supprimer un element de la BDD
def delete_one(id: str):
    results = collection.delete_one({"_id": ObjectId(id)})
    return results

# Fonction permettant de supprimer plusieurs elements de la BDD
def delete_many(filter: dict):
    results = collection.delete_many(filter)
    return results
