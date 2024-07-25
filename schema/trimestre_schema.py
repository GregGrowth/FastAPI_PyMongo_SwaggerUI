from pydantic import BaseModel, constr
from typing import Optional

# Schema pour structurer les donnees pour la fonction Insert
class TrimestreInsertSchema(BaseModel):
    idtrimestre: str = constr(min_length=1, max_length=1)
    nom: str = constr(min_length=1)
    date: Optional[str] = None

# Schema pour structurer les donnees pour la fonction Update
class TrimestreUpdateSchema(BaseModel):
    nom: Optional[str] = None
    date: Optional[str] = None