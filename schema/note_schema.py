from pydantic import BaseModel
from typing import Optional

# Schema pour structurer les donnees pour la fonction Update
class NoteUpdateSchema(BaseModel):
    date_saisie: Optional[str] = None
    note: Optional[str] = None
    avis: Optional[str] = None
    avancement: Optional[str] = None

# Schema pour structurer les donnees pour la fonction Insert
class NoteInsertSchema(BaseModel):
    date_saisie: str
    ideleve: str
    idclasse: str
    idmatiere: str
    idprof: str
    idtrimestre: str
    note: str
    avis: Optional[str]
    avancement: Optional[str]

'''
class NoteSchemaInsertId(NoteSchemaInsert):
    idnotes: str
'''