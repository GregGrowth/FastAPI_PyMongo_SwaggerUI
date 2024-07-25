from pydantic import BaseModel, constr
from typing import Optional

# Schema pour structurer les donnees pour la fonction Insert
class MatiereInsertSchema(BaseModel):
    idmatiere: str = constr(min_length=1, max_length=1)
    nom: str = constr(min_length=1)

# Schema pour structurer les donnees pour la fonction Update
class MatiereUpdateSchema(BaseModel):
    nom: str = constr(min_length=1)