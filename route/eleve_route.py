from fastapi import APIRouter
from service import eleve_service
from schema.eleve_schema import EleveUpdateSchema, EleveInsertSchema
from typing import List

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
@router.post("/one", response_model=dict)
def create_one_eleve(item: EleveInsertSchema):
    item_dict = item.dict(exclude_unset=True)  # On exclut les donnees de type None (= donnees non renseignees)
    results = eleve_service.create_one(item_dict)
    return {"acknowledged": results.acknowledged}

# Ajout d'une fonction permettant d'inserer plusieurs elements de la BDD
@router.post("/many", response_model=dict)
def create_many_eleve(item: List[EleveInsertSchema]):
    item_dict = []
    # On exclut les donnees de type None (= donnees non renseignees) dans chaque element
    for i in range(len(item)):
        item_dict.append(item[i].dict(exclude_unset=True))
    results = eleve_service.create_many(item_dict)
    return {"acknowledged": results.acknowledged}


# Ajout d'une fonction permettant de mettre a jour la classe d'un eleve de la BDD
@router.patch("/one/{id_eleve}", response_model=dict)
def update_one_eleve(id_eleve, update: EleveUpdateSchema):
    update_dict = update.dict(exclude_unset=True)   # On exclut les donnees de type None (= donnees non renseignees)
    results = eleve_service.update_one(id_eleve, update_dict)
    return {"modified_count": results.modified_count}

# Ajout d'une fonction permettant de mettre a jour plusieurs elements de la BDD
@router.patch("/many/{filter}", response_model=dict)
def update_many_eleve(filter: dict, item: List[EleveUpdateSchema]):
    item_dict = []
    # On exclut les donnees de type None (= donnees non renseignees) dans chaque element
    for i in range(len(item)):
        item_dict.append(item[i].dict(exclude_unset=True))
    results = eleve_service.update_many(filter, item_dict)
    return {"acknowledged": results.acknowledged}

# Ajout d'une fonction permettant de supprimer un element de la BDD
@router.delete("/one/{id}", response_model=dict)
def delete_one_eleve(id):
    results = eleve_service.delete_one(id)
    return {"deleted_count": results.deleted_count}

# Ajout d'une fonction permettant de supprimer plusieurs elements de la BDD
@router.delete("/many/{item}", response_model=dict)
def delete_many_eleve(item):
    results = eleve_service.delete_many(item)
    return {"deleted_count": results.deleted_count}

