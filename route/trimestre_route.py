from fastapi import APIRouter
from service import trimestre_service

# Initailisation du router
router = APIRouter(
    prefix="/trimestre",
    tags=["Trimestre"]
)

# Ajout d'une fonction permettant d'afficher un element de la BDD
@router.get("/{id}")
def get_one_trimestre(id):
    return trimestre_service.get_one(id)

# Ajout d'une fonction permettant d'afficher plusieurs elements de la BDD
@router.get("/")
def get_all_trimestre():
    return trimestre_service.get_all()

# Ajout d'une fonction permettant d'inserer un element de la BDD
@router.post("/one")
def create_one_trimestre(item):
    return trimestre_service.create_one(item)

# Ajout d'une fonction permettant d'inserer plusieurs elements de la BDD
@router.post("/many")
def create_many_trimestre(item):
    return trimestre_service.creat_many(item)

"""
# Ajout d'une fonction permettant de mettre a jour un element de la BDD
@router.patch("/one")
def update_one_trimestre(filter, newValue):
    return trimestre_service.update_one(filter, newValue)

# Ajout d'une fonction permettant de mettre a jour plusieurs elements de la BDD
@router.patch("/many")
def update_many_trimestre(filter, newValue):
    return trimestre_service.update_many(filter, newValue)
"""
# Ajout d'une fonction permettant de supprimer un element de la BDD
@router.delete("/one/{id}")
def delete_one_trimestre(id):
    return trimestre_service.delete_one(id)

# Ajout d'une fonction permettant de supprimer plusieurs elements de la BDD
@router.delete("/many/{item}")
def delete_many_trimestre(item):
    return trimestre_service.delete_many(item)