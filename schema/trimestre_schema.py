from pydantic import BaseModel
from typing import Optional

class TrimestreUpdateSchema(BaseModel):
    nom: Optional[str] = None
    date: Optional[str] = None