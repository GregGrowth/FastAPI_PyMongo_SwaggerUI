from fastapi import APIRouter
from service import classe_service
from schema.classe_schema import ClasseUpdateSchema

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
@router.post("/one")
def create_one_classe(item):
    return classe_service.create_one(item)

# Ajout d'une fonction permettant d'inserer plusieurs elements de la BDD
@router.post("/many")
def create_many_classe(item):
    return classe_service.create_many(item)

# Ajout d'une fonction permettant de mettre a jour le nom d'une classe de la BDD
@router.patch("/one/{id_classe}", response_model=dict)
def update_one_classe(id_classe: str, update: ClasseUpdateSchema):
    update_dict = update.dict(exclude_unset=True)   # On exclut les donnees de type None (= donnees non renseignees)
    results = classe_service.update_one(id_classe, update_dict)
    return {"modified_count": results.modified_count}

"""
# Ajout d'une fonction permettant de mettre a jour plusieurs elements de la BDD
@router.patch("/many")
def update_many_classe(filter, newValue):
    return classe_service.update_many(filter, newValue)
"""
# Ajout d'une fonction permettant de supprimer un element de la BDD
@router.delete("/one/{id}")
def delete_one_classe(id):
    return classe_service.delete_one(id)

# Ajout d'une fonction permettant de supprimer plusieurs elements de la BDD
@router.delete("/many/{item}")
def delete_many_classe(item):
    return classe_service.delete_many(item)

@router.get("/q3")
async def read_eleve_classe_choix(id: int):
    eleve_classe_choix = classe_service.find({"classe": id}, {"_id": 0})
    return list(eleve_classe_choix)
