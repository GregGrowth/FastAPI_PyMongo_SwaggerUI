from fastapi import FastAPI
from route import classe_route, eleve_route, matiere_route, note_route, professeur_route, trimestre_route
import uvicorn
import webbrowser
import threading

# Initialiation de l'application avec FastAPI
app = FastAPI()
app.include_router(classe_route.router)
app.include_router(eleve_route.router)
app.include_router(matiere_route.router)
app.include_router(note_route.router)
app.include_router(professeur_route.router)
app.include_router(trimestre_route.router)


# Fonction permettant d'ouvrir notre appli FastAPI
def open_docs():
    webbrowser.open_new("http://127.0.0.1:8000")
    webbrowser.open_new("http://127.0.0.1:8000/docs")


# Démarrage automatique de notre application en définissant un délai d'ouverture
if __name__ == "__main__":
    threading.Timer(2.0, open_docs).start()
    uvicorn.run(app, host="127.0.0.1", port=8000)
