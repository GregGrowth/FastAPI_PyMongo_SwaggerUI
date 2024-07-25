from pydantic import BaseModel
from typing import Optional

# Schema pour structurer les donnees pour la fonction Insert
class EleveInsertSchema(BaseModel):
    id: str
    nom: str
    prenom: str
    classe: str
    date_naissance: Optional[str]
    adresse: Optional[str]
    sexe: Optional[str]

# Schema pour structurer les donnees pour la fonction Update
class EleveUpdateSchema(BaseModel):
    nom: Optional[str] = None
    prenom: Optional[str] = None
    classe: Optional[str] = None
    date_naissance: Optional[str] = None
    adresse: Optional[str] = None
    sexe: Optional[str] = None

# Ajout pour Q3
class Q3(BaseModel):
    id: str
    nom: str
    prenom: str
    classe: str
    date_naissance: str
    adresse: str
    sexe: str