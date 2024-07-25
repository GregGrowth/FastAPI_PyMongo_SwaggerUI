from pydantic import BaseModel
from typing import Optional

class ProfesseurSchemaInsert(BaseModel):
    id: str
    nom: str
    prenom: str
    classe: str
    date_naissance: str
    adresse: str
    sexe: str

class ProfesseurUpdateSchema(BaseModel):
    nom: Optional[str] = None
    prenom: Optional[str] = None
    classe: Optional[str] = None
    date_naissance: Optional[str] = None
    adresse: Optional[str] = None
    sexe: Optional[str] = None