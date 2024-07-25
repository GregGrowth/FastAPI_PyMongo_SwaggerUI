from pydantic import BaseModel
from typing import Optional

# Schema pour structurer les donnees pour la fonction Insert
class ClasseInsertSchema(BaseModel):
    id: str
    nom: str
    prof: str

# Schema pour structurer les donnees pour la fonction Update
class ClasseUpdateSchema(BaseModel):
    nom: Optional[str] = None
    prof: Optional[str] = None

