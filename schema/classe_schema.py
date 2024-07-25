from pydantic import BaseModel, constr
from typing import Optional

# Schema pour structurer les donnees pour la fonction Insert
class ClasseInsertSchema(BaseModel):
    id: str = constr(min_length=1, max_length=1)
    nom: str = constr(min_length=1, max_length=1)
    prof: Optional[str] = None

# Schema pour structurer les donnees pour la fonction Update
class ClasseUpdateSchema(BaseModel):
    nom: Optional[str] = None
    prof: Optional[str] = None
