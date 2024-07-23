from fastapi import FastAPI
from route import classe_route, eleve_route, matiere_route, note_route, professeur_route, trimestre_route
import uvicorn

# Initialiation de l'application avec FastAPI
app = FastAPI()
app.include_router(classe_route.router)
app.include_router(eleve_route.router)
app.include_router(matiere_route.router)
app.include_router(note_route.router)
app.include_router(professeur_route.router)
app.include_router(trimestre_route.router)

# Démarrer l'application avec uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
