from db import database
from bson import ObjectId

# Selectionner la base de donnees (BDD)
collection = database["note"]

# Fonction permettant d'afficher un element de la BDD
def get_one(id: str):
    results = collection.find_one({"_id": ObjectId(id)}, {"_id": 0})
    return results

# Fonction permettant d'afficher plusieurs elements de la BDD
def get_all():
    results = collection.find({}, {"_id": 0})
    return list(results)

# Fonction permettant d'inserer un element de la BDD
def create_one(item: dict):
    results = collection.insert_one(item)
    return results

# Fonction permettant d'inserer plusieurs elements de la BDD
def create_many(item: dict):
    results = collection.insert_many(item)
    return results

"""
# Fonction permettant de mettre a jour un element de la BDD
def update_one(filter, newValue):
    results = collection.update_one(filter, newValue)
    return results

# Fonction permettant de mettre a jour plusieurs elements de la BDD
def update_many(filter, newValue):
    results = collection.update_many(filter, newValue)
    return results
"""

# Fonction permettant de supprimer un element de la BDD
def delete_one(id: str):
    results = collection.delete_one(ObjectId(id))
    return results

# Fonction permettant de supprimer plusieurs elements de la BDD
def delete_many(filter: dict):
    results = collection.delete_many(filter)
    return results

from db import database
from bson import ObjectId

# Sélection des collections
eleve_collection = database["eleve"]
note_collection = database["note"]

def get_eleve_notes_par_prof(professeur_id: str):
    pipeline = [
        {
            "$match": {
                "idprof": professeur_id  # Filtrer les notes pour le professeur spécifié
            }
        },
        {
            "$lookup": {
                "from": "eleve",
                "localField": "ideleve",
                "foreignField": "id",
                "as": "eleve_details"
            }
        },
        {
            "$unwind": "$eleve_details"  # Déplier les détails des élèves
        },
        {
            "$project": {
                "_id": 0,
                "eleve_id": "$eleve_details.id",
                "nom": "$eleve_details.nom",
                "prenom": "$eleve_details.prenom",
                "note": "$note"
            }
        }
    ]
    results = note_collection.aggregate(pipeline)
    return list(results)