
from pydantic import BaseModel,constr,Field
from typing import Annotated

#Fichier modele pour définir les données dans chaque collection
class Classe(BaseModel):
    id: constr(min_length=1, max_length=1)
    nom: str
    prof: str

class Eleve(BaseModel):
    id: str = constr (min_length=1, max_length=1)
    nom: str
    prenom: str
    classe: str
    date_naissance: str
    adresse: str
    sexe: str

class Matiere(BaseModel):
    idmatiere: str
    nom: str

class Note(BaseModel):
    idnotes: str
    date_saisie: str
    ideleve: str
    idclasse: str
    idmatiere: str
    idprof: str
    idtrimestre: str
    note: str
    avis: str
    avancement: str

class Professeur(BaseModel):
    id: str
    nom: str
    prenom: str
    date_naissance: str
    adresse: str
    sexe: str

class Trimestre(BaseModel):
    idtrimestre: str
    nom: str
    date: str

