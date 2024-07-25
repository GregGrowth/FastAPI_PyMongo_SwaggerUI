from pydantic import BaseModel
from typing import Optional

# Schema pour structurer les donnees pour la fonction Insert
class MatiereInsertSchema(BaseModel):
    idmatiere: str
    nom: str

# Schema pour structurer les donnees pour la fonction Update
class MatiereUpdateSchema(BaseModel):
    nom: str