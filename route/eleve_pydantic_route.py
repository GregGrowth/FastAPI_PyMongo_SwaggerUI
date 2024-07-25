from fastapi import APIRouter,HTTPException
from service import eleve_pydantic_service
from route.models import Eleve
from typing import List
from fastapi.encoders import jsonable_encoder
# Initialisation du router
router = APIRouter(
    prefix="/elevePydantic",
    tags=["ElevePy"]
)

@router.get("/classe2/{idclasse}",response_model=List[Eleve])
def read_eleve_classe_choix_PY(idclasse:str):
        eleves = eleve_pydantic_service.read_eleve_classe_choix_PY(idclasse)
        if  eleves :
            return eleves
        raise HTTPException(status_code=404, detail="Eleve not found")


