from pydantic import BaseModel, constr
from typing import Optional

# Schema pour structurer les donnees pour la fonction Insert
class EleveInsertSchema(BaseModel):
    id: str = constr(min_length=1, max_length=3)
    nom: str = constr(min_length=1)
    prenom: str = constr(min_length=1)
    classe: str = constr(min_length=1, max_length=1)
    date_naissance: Optional[str] = None
    adresse: Optional[str] = None
    sexe: Optional[str] = None

# Schema pour structurer les donnees pour la fonction Update
class EleveUpdateSchema(BaseModel):
    nom: Optional[str] = None
    prenom: Optional[str] = None
    classe: Optional[str] = None
    date_naissance: Optional[str] = None
    adresse: Optional[str] = None
    sexe: Optional[str] = None