from fastapi import APIRouter
from service import matiere_service
from schema.matiere_schema import MatiereUpdateSchema, MatiereInsertSchema
from typing import List


# Initailisation du router
router = APIRouter(
    prefix="/matiere",
    tags=["Matiere"]
)

# Ajout d'une fonction permettant d'afficher un element de la BDD
@router.get("/{id}")
def get_one_matiere(id):
    return matiere_service.get_one(id)

# Ajout d'une fonction permettant d'afficher plusieurs elements de la BDD
@router.get("/")
def get_all_matiere():
    return matiere_service.get_all()

# Ajout d'une fonction permettant d'inserer un element de la BDD
@router.post("/one", response_model=dict)
def create_one_matiere(item: MatiereInsertSchema):
    item_dict = item.dict(exclude_unset=True)  # On exclut les donnees de type None (= donnees non renseignees)
    results = matiere_service.create_one(item_dict)
    return {"acknowledged": results.acknowledged}

# Ajout d'une fonction permettant d'inserer plusieurs elements de la BDD
@router.post("/many", response_model=dict)
def create_many_matiere(item: List[MatiereInsertSchema]):
    item_dict = []
    # On exclut les donnees de type None (= donnees non renseignees) dans chaque element
    for i in range(len(item)):
        item_dict.append(item[i].dict(exclude_unset=True))
    results = matiere_service.create_many(item_dict)
    return {"acknowledged": results.acknowledged}

# Ajout d'une fonction permettant de mettre le nom d'une matiere de la BDD
@router.patch("/one/{id_matiere}", response_model=dict)
def update_one_matiere(id_matiere, update: MatiereUpdateSchema):
    update_dict = update.dict(exclude_unset=True)  # On exclut les donnees de type None (= donnees non renseignees)
    results = matiere_service.update_one(id_matiere, update_dict)
    return {"modified_count": results.modified_count}

# Ajout d'une fonction permettant de mettre a jour plusieurs elements de la BDD
@router.patch("/many/{filter}", response_model=dict)
def update_many_matiere(filter: dict, item: List[MatiereUpdateSchema]):
    item_dict = []
    # On exclut les donnees de type None (= donnees non renseignees) dans chaque element
    for i in range(len(item)):
        item_dict.append(item[i].dict(exclude_unset=True))
    results = matiere_service.update_many(filter, item_dict)
    return {"acknowledged": results.acknowledged}

# Ajout d'une fonction permettant de supprimer un element de la BDD
@router.delete("/one/{id}", response_model=dict)
def delete_one_matiere(id):
    results = matiere_service.delete_one(id)
    return {"deleted_count": results.deleted_count}

# Ajout d'une fonction permettant de supprimer plusieurs elements de la BDD
@router.delete("/many/{item}", response_model=dict)
def delete_many_matiere(item):
    results = matiere_service.delete_many(item)
    return {"deleted_count": results.deleted_count}