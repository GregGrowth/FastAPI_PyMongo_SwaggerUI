from fastapi import APIRouter
from service import trimestre_service
from schema.trimestre_schema import TrimestreUpdateSchema, TrimestreInsertSchema
from typing import List

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
@router.post("/one", response_model=dict)
def create_one_trimestre(item: TrimestreInsertSchema):
    item_dict = item.dict(exclude_unset=True)  # On exclut les donnees de type None (= donnees non renseignees)
    results = trimestre_service.create_one(item_dict)
    return {"acknowledged": str(results.acknowledged)}

# Ajout d'une fonction permettant d'inserer plusieurs elements de la BDD
@router.post("/many", response_model=dict)
def create_many_trimestre(item: List[TrimestreInsertSchema]):
    item_dict = []
    # On exclut les donnees de type None (= donnees non renseignees) dans chaque element
    for i in range(len(item)):
        item_dict.append(item[i].dict(exclude_unset=True))
    results = trimestre_service.create_many(item_dict)
    return {"acknowledged": results.acknowledged}

# Ajout d'une fonction permettant de mettre a jour la date d'un trimestre de la BDD
@router.patch("/one/{id_trimestre}", response_model=dict)
def update_one_trimestre(id_trimestre, update: TrimestreUpdateSchema):
    update_dict = update.dict(exclude_unset=True)  # On exclut les donnees de type None (= donnees non renseignees)
    results = trimestre_service.update_one(id_trimestre, update_dict)
    return {"modified_count": results.modified_count}

# Ajout d'une fonction permettant de mettre a jour plusieurs elements de la BDD
@router.patch("/many", response_model=dict)
def update_many_trimestre(filter: dict, item: List[TrimestreUpdateSchema]):
    item_dict = []
    # On exclut les donnees de type None (= donnees non renseignees) dans chaque element
    for i in range(len(item)):
        item_dict.append(item[i].dict(exclude_unset=True))
    results = trimestre_service.update_many(filter, item_dict)
    return {"acknowledged": results.acknowledged}

# Ajout d'une fonction permettant de supprimer un element de la BDD
@router.delete("/one/{id}", response_model=dict)
def delete_one_trimestre(id):
    results = trimestre_service.delete_one(id)
    return {"deleted_count": results.deleted_count}

# Ajout d'une fonction permettant de supprimer plusieurs elements de la BDD
@router.delete("/many/{item}", response_model=dict)
def delete_many_trimestre(item):
    results = trimestre_service.delete_many(item)
    return {"deleted_count": results.deleted_count}