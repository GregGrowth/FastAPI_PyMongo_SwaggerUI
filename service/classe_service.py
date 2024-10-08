from db import database
from bson import ObjectId

# Selectionner la base de donnees (BDD)
collection = database["classe"]

# Fonction permettant d'afficher un element de la BDD
def get_one(id: str):
    results = collection.find_one({"_id": ObjectId(id)}, {"_id": 0})
    return results

# Fonction permettatn d'afficher les eleves par classe
def get_eleve_by_classe():
    results = collection.aggregate([
        # On garde uniquement les elements qui nous interessent pour l'affichage des eleves par classe
        {
            "$project": {"_id": 0, "prof": 0}
        },
        # On effectue un LEFT OUTTER JOIN avec la table `eleve`
        {
            "$lookup":{
                "from": "eleve",
                "localField": "id",
                "foreignField": "classe",
                "as": "eleve_by_classe"
            }
        },
        # On décompose le resultats du lookup pour pouvoir plus facilement les manipuler par la suite
        {
            "$unwind": "$eleve_by_classe"
        },
        # On garde uniquement les elements qui nous interessent pour l'affichage des eleves par classe
        {
            "$project": {"id": 0, "eleve_by_classe": {"_id": 0, "classe": 0, "id": 0, "date_naissance": 0, "adresse": 0, "sexe": 0}}
        },
        # On regroupe le resultats par classe
        {
            "$group":
            {
                "_id": {"classe": "$nom"},
                "list_eleves": {
                    "$push": {"nom": "$eleve_by_classe.nom", "prenom": "$eleve_by_classe.prenom"}
                }
            }
        }
    ])
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

# Fonction permettant de mettre a jour le nom d'une classe de la BDD
def update_one(id_classe: str, update: dict):
    results = collection.update_one({"id": id_classe}, {"$set": update})
    return results

# Fonction permettant de mettre a jour plusieurs elements de la BDD
def update_many(filter, newValue):
    results = collection.update_many(filter, newValue)
    return results

# Fonction permettant de supprimer un element de la BDD
def delete_one(id: str):
    results = collection.delete_one(ObjectId(id))
    return results

# Fonction permettant de supprimer plusieurs elements de la BDD
def delete_many(filter: dict):
    results = collection.delete_many(filter)
    return results
