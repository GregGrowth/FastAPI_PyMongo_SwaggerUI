from fastapi import APIRouter
from service import classe_service
from schema.classe_schema import ClasseUpdateSchema, ClasseInsertSchema
from typing import List

# Initailisation du router
router = APIRouter(
    prefix="/classe",
    tags=["Classe"]
)

# Ajout d'une fonction permettant d'afficher un element de la BDD
@router.get("/{id}")
def get_one_classe(id):
    return classe_service.get_one(id)

# Ajout d'une fonction permettant d'afficher les eleves par classe
@router.get("/q2_eleve_by_classe/all_classe")
def get_eleve_by_classe():
    return classe_service.get_eleve_by_classe()

# Ajout d'une fonction permettant d'afficher plusieurs elements de la BDD
@router.get("/")
def get_all_classe():
    return classe_service.get_all()

# Ajout d'une fonction permettant d'inserer un element de la BDD
@router.post("/one", response_model=dict)
def create_one_classe(item: ClasseInsertSchema):
    item_dict = item.dict(exclude_unset=True)  # On exclut les donnees de type None (= donnees non renseignees)
    results = classe_service.create_one(item_dict)
    return {"acknowledged": results.acknowledged}

# Ajout d'une fonction permettant d'inserer plusieurs elements de la BDD
@router.post("/many", response_model=dict)
def create_many_classe(item: List[ClasseInsertSchema]):
    item_dict = []
    # On exclut les donnees de type None (= donnees non renseignees) dans chaque element
    for i in range(len(item)):
        item_dict.append(item[i].dict(exclude_unset=True))
    results = classe_service.create_many(item_dict)
    return {"acknowledged": results.acknowledged}

# Ajout d'une fonction permettant de mettre a jour le nom d'une classe de la BDD
@router.patch("/one/{id_classe}", response_model=dict)
def update_one_classe(id_classe: str, update: ClasseUpdateSchema):
    update_dict = update.dict(exclude_unset=True)   # On exclut les donnees de type None (= donnees non renseignees)
    results = classe_service.update_one(id_classe, update_dict)
    return {"modified_count": results.modified_count}

# Ajout d'une fonction permettant de mettre a jour plusieurs elements de la BDD
@router.patch("/many/{filter}", response_model=dict)
def update_many_classe(filter: dict, item: List[ClasseUpdateSchema]):
    item_dict = []
    # On exclut les donnees de type None (= donnees non renseignees) dans chaque element
    for i in range(len(item)):
        item_dict.append(item[i].dict(exclude_unset=True))
    results = classe_service.update_many(filter, item_dict)
    return {"acknowledged": results.acknowledged}

# Ajout d'une fonction permettant de supprimer un element de la BDD
@router.delete("/one/{id}", response_model=dict)
def delete_one_classe(id):
    results = classe_service.delete_one(id)
    return {"deleted_count": results.deleted_count}

# Ajout d'une fonction permettant de supprimer plusieurs elements de la BDD
@router.delete("/many/{item}", response_model=dict)
def delete_many_classe(item):
    results = classe_service.delete_many(item)
    return {"deleted_count": results.deleted_count}

