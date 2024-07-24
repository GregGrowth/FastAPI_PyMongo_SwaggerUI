from fastapi import APIRouter
from service import eleve_service

# Initailisation du router
router = APIRouter(
    prefix="/eleve",
    tags=["Eleve"]
)

# Ajout d'une fonction permettant d'afficher un element de la BDD
@router.get("/{id}")
def get_one_eleve(id):
    return eleve_service.get_one(id)

# Ajout d'une fonction permettant d'afficher les eleves selon le choix d'une classe
@router.get("/q3_eleve_choose_classe/{idclasse}")
def get_eleve_choose_classe(idclasse):
    return eleve_service.get_eleve_choose_classe(idclasse)

# Ajout d'une fonction permettant d'afficher plusieurs elements de la BDD
@router.get("/")
def get_all_eleve():
    return eleve_service.get_all()

# Ajout d'une fonction permettant d'inserer un element de la BDD
@router.post("/one")
def create_one_eleve(item):
    return eleve_service.create_one(item)

# Ajout d'une fonction permettant d'inserer plusieurs elements de la BDD
@router.post("/many")
def create_many_eleve(item):
    return eleve_service.creat_many(item)

"""
# Ajout d'une fonction permettant de mettre a jour un element de la BDD
@router.patch("/one")
def update_one_eleve(filter, newValue):
    return eleve_service.update_one(filter, newValue)

# Ajout d'une fonction permettant de mettre a jour plusieurs elements de la BDD
@router.patch("/many")
def update_many_eleve(filter, newValue):
    return eleve_service.update_many(filter, newValue)
"""
# Ajout d'une fonction permettant de supprimer un element de la BDD
@router.delete("/one/{id}")
def delete_one_eleve(id):
    return eleve_service.delete_one(id)

# Ajout d'une fonction permettant de supprimer plusieurs elements de la BDD
@router.delete("/many/{item}")
def delete_many_eleve(item):
    return eleve_service.delete_many(item)

