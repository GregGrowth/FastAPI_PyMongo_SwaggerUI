# Projet NOSQL & PYTHON / DIGINAMIC

## Description du Projet
L’objectif du projet a été de développer une API fonctionnelle qui permet pouvoir récupérer les données suivantes à partir d’une API Python (avec FASTAPI et PyMongo). Pour les besoins de l’exercice, nous avons du transformer une BDD SQL en une BDD NoSQL.

## Membres du Projet et équipe de développement

Mélissa KUNEGEL
Lucas FANGET
Grégoire DELCROIX

## Coordinateur et Suivi

Robin HOTTON
Christophe GERMAIN

## Architecture du Projet

📂 Dossier service : contient les fonctionnalités nécessaires et demandées.\
📂 Dossier route : contient les routes de l'API.\
📂 Dossier schema : contient les schemas pydantic qui assurent la validation et la sérialisation des données et améliorent la sécurité des types.\
Fichier main.py : point d'entrée principal de l'application FastAPI.\
Fichier db.py : Configuration de la connexion à la base de données NoSQL.\
Fichier requirements.txt : utile pour la gestion des dépendances et l'installation des bibliothèques.\
Fichier .gitignore : fichiers à ignorer par Git.\
Fichier .env : variables d'environnement pour la configuration.

## Fonctionnalités obligatoires pour répondre au cahier des charges
- Récupérer la liste des professeurs
- Récupérer la liste des élèves par classe
- Récupérer la liste des élèves selon une classe donnée
- Récupérer les notes d'un élève
- Récupérer les élèves et leurs notes selon un professeur

## Prérequis Techniques
- Python 3.11.9
- PyMongo 3.8
- pip (gestionnaire de paquets Python)

## Installation

### Étapes d'installation
1. Clonez le dépôt du projet :
    ```bash
    git clone <url_du_projet>
    cd <nom_du_dossier_du_projet>
    ```

2. Créez un environnement virtuel et activez-le :
    ```bash
    python -m venv venv
    source venv/bin/activate # Sur Windows : venv\Scripts\activate
    ```

3. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

### Configuration des BDD
4. Configurez les variables d'environnement dans le fichier `.env`. Exemple de configuration :
    ```
   USER="username"
   PASSWORD="mdp"
   CLUSTER="cluster0.pfx6cet"
   DB_NAME="digischool"
    ```
   exemple : uri = f"mongodb+srv://{user_encoded}:{pwd_encoded}@{cluster}.mongodb.net/"
   Pensez à créer un utilisateur pour accéder à la base de donnée sur MongoDB.

## Utilisation de uvicorn et swagger UI

 Tapez : uvicorn main:app --reload
 Cliquez : http://127.0.0.1:8000
 Ajoutez à l’url : http://127.0.0.1:8000/docs
