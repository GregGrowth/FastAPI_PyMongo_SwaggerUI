from pydantic import BaseModel, constr
from typing import Optional

# Schema pour structurer les donnees pour la fonction Insert
class NoteInsertSchema(BaseModel):
    idnotes: str = constr(min_length=1, max_length=1)
    date_saisie: Optional[str] = None
    ideleve: str = constr(min_length=1, max_length=1)
    idclasse: Optional[str] = None
    idmatiere: Optional[str] = None
    idprof: Optional[str] = None
    idtrimestre: Optional[str] = None
    note: str = constr(min_length=1)
    avis: Optional[str] = None
    avancement: Optional[str] = None

# Schema pour structurer les donnees pour la fonction Update
class NoteUpdateSchema(BaseModel):
    date_saisie: Optional[str] = None
    note: Optional[str] = None
    avis: Optional[str] = None
    avancement: Optional[str] = None




