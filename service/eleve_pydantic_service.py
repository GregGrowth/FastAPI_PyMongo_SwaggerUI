from db import database
from route.models import Eleve
from route.models import Classe
from typing import List
from fastapi import HTTPException


# Selectionner la base de donnees (BDD)
collection = database["eleve"]


# Fonction permettant d'afficher les eleves d'une classe
def read_eleve_classe_choix_PY(idclasse: str) -> List[Eleve]:
    results = collection.find({"classe": idclasse}, {"_id": 0})
    eleves = [Eleve(**result) for result in results]
    if eleves:
        return eleves
    else:
        raise HTTPException(status_code=404, detail="Eleve not found")




