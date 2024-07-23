from fastapi import APIRouter
from service import professeur_service

# Initailisation du router
router = APIRouter(
    prefix="/professeur",
    tags=["Professeur"]
)

# Ajout d'un fonction permettant d'afficher un element de la BDD
@router.get("/{id}")
def get_one_professeur(id):
    return professeur_service.get_one(id)

# Ajout d'un fonction permettant d'afficher plusieurs elements de la BDD
@router.get("/")
def get_all_professeur():
    return professeur_service.get_all()

# Ajout d'un fonction permettant d'inserer un element de la BDD
@router.post("/one")
def create_one_professeur(item):
    return professeur_service.create_one(item)

# Ajout d'un fonction permettant d'inserer plusieurs elements de la BDD
@router.post("/many")
def create_many_professeur(item):
    return professeur_service.creat_many(item)

"""
# Ajout d'un fonction permettant de mettre a jour un element de la BDD
@router.patch("/one")
def update_one_professeur(filter, newValue):
    return professeur_service.update_one(filter, newValue)

# Ajout d'un fonction permettant de mettre a jour plusieurs elements de la BDD
@router.patch("/many")
def update_many_professeur(filter, newValue):
    return professeur_service.update_many(filter, newValue)
"""
# Ajout d'un fonction permettant de supprimer un element de la BDD
@router.delete("/one/{id}")
def delete_one_professeur(id):
    return professeur_service.delete_one(id)

# Ajout d'un fonction permettant de supprimer plusieurs elements de la BDD
@router.delete("/many/{item}")
def delete_many_professeur(item):
    return professeur_service.delete_many(item)