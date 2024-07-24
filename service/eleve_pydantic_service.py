from db import database
from route.models import Eleve
from typing import List


# Selectionner la base de donnees (BDD)
collection = database["eleve"]


# Fonction permettant d'afficher les eleves d'une classe
def read_eleve_classe_choix_PY(idclasse: str) -> List[Eleve]:
    results = collection.find({"classe": idclasse}, {"_id": 0})
    return [Eleve(**result) for result in results]


