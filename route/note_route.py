from fastapi import APIRouter
from service import note_service

# Initailisation du router
router = APIRouter(
    prefix="/note",
    tags=["Note"]
)

# Ajout d'un fonction permettant d'afficher un element de la BDD
@router.get("/{id}")
def get_one_note(id):
    return note_service.get_one(id)

# Ajout d'un fonction permettant d'afficher les notes d'un eleve
@router.get("/eleve/{ideleve}")
def get_note_eleve(ideleve):
    return note_service.get_note_eleve(ideleve)

# Ajout d'un fonction permettant d'afficher plusieurs elements de la BDD
@router.get("/")
def get_all_note():
    return note_service.get_all()

# Ajout d'un fonction permettant d'inserer un element de la BDD
@router.post("/one")
def create_one_note(item):
    return note_service.create_one(item)

# Ajout d'un fonction permettant d'inserer plusieurs elements de la BDD
@router.post("/many")
def create_many_note(item):
    return note_service.creat_many(item)

"""
# Ajout d'un fonction permettant de mettre a jour un element de la BDD
@router.patch("/one")
def update_one_note(filter, newValue):
    return note_service.update_one(filter, newValue)

# Ajout d'un fonction permettant de mettre a jour plusieurs elements de la BDD
@router.patch("/many")
def update_many_note(filter, newValue):
    return note_service.update_many(filter, newValue)
"""
# Ajout d'un fonction permettant de supprimer un element de la BDD
@router.delete("/one/{id}")
def delete_one_note(id):
    return note_service.delete_one(id)

# Ajout d'un fonction permettant de supprimer plusieurs elements de la BDD
@router.delete("/many/{item}")
def delete_many_note(item):
    return note_service.delete_many(item)