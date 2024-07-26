from fastapi import APIRouter
from service import note_service
from schema.note_schema import NoteUpdateSchema, NoteInsertSchema
from typing import List

# Initailisation du router
router = APIRouter(
    prefix="/note",
    tags=["Note"]
)

# Ajout d'une fonction permettant d'afficher un element de la BDD
@router.get("/{id}")
def get_one_note(id):
    return note_service.get_one(id)

# Ajout d'une fonction permettant d'afficher les notes d'un eleve
@router.get("/q4_note_choose_eleve/{ideleve}")
def get_note_choose_eleve(ideleve):
    return note_service.get_note_choose_eleve(ideleve)

# Ajout d'une fonction permettant d'afficher plusieurs elements de la BDD
@router.get("/")
def get_all_note():
    return note_service.get_all()

# Ajout d'une fonction permettant d'inserer un element de la BDD
@router.post("/one", response_model=dict)
def create_one_note(item: NoteInsertSchema):
    item_dict = item.dict(exclude_unset=True)  # On exclut les donnees de type None (= donnees non renseignees)
    results = note_service.create_one(item_dict)
    return {"acknowledged": results.acknowledged}

# Ajout d'une fonction permettant d'inserer plusieurs elements de la BDD
@router.post("/many", response_model=dict)
def create_many_note(item: List[NoteInsertSchema]):
    item_dict = []
    # On exclut les donnees de type None (= donnees non renseignees) dans chaque element
    for i in range(len(item)):
        item_dict.append(item[i].dict(exclude_unset=True))
    results = note_service.create_many(item_dict)
    return {"acknowledged": results.acknowledged}

# Ajout d'une fonction permettant de mettre a jour un element de la BDD
@router.patch("/one/{id_note}", response_model=dict)
def update_one_note(id_note: str, update: NoteUpdateSchema):
    update_dict = update.dict(exclude_unset=True)  # On exclut les donnees de type None (= donnees non renseignees)
    results = note_service.update_one(id_note, update_dict)
    return {"modified_count": results.modified_count}

# Ajout d'une fonction permettant de mettre a jour plusieurs elements de la BDD
@router.patch("/many/{filter}", response_model=dict)
def update_many_note(filter: dict, item: List[NoteUpdateSchema]):
    item_dict = []
    # On exclut les donnees de type None (= donnees non renseignees) dans chaque element
    for i in range(len(item)):
        item_dict.append(item[i].dict(exclude_unset=True))
    results = note_service.update_many(filter, item_dict)
    return {"acknowledged": results.acknowledged}

# Ajout d'une fonction permettant de supprimer un element de la BDD
@router.delete("/one/{id}", response_model=dict)
def delete_one_note(id):
    results = note_service.delete_one(id)
    return {"deleted_count": results.deleted_count}

# Ajout d'une fonction permettant de supprimer plusieurs elements de la BDD
@router.delete("/many/{item}", response_model=dict)
def delete_many_note(item):
    results = note_service.delete_many(item)
    return {"deleted_count": results.deleted_count}