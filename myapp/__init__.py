# coding:utf-8

"""
Usine à application

https://hackersandslackers.com/flask-application-factory/

"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config


db = SQLAlchemy() # On la crée vide


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)      # Configuration de base de l'application dans l'objet config
    app.config.from_pyfile('config.py') # Configuration particulières de l'instance

    db.init_app(app) # + db = SQLAlhemyq() -> equivaut à db = SQLAlchemy(app)

    """
    Ici on va avoir un problème de dépendences circulaire si on utilise pas le gestionnaire de contexte.
    En effet on import "main", qui importe models, qui import cvs_utils. cvs_utils doit accéder à app.config[] pour 
    pouvoir fonctionner.
    MAIS app n'est pas encore créer en totalité ... Donc on va utiliser current_app.config[] qui permet de contourner la 
    dépendence circulaire. Toutefois current_app.config[] ne "push" pas automatiquement le context, en effet current_app
    est lié à l'application courante, le gestionnaire de context étant associé à une application particulière, current_app
    ne peut savoir laquelle (l'application n'est pas identifiée par current_app, il s'agit juste de l'application en 
    train de tourner ...) On place donc la suite du code (et la chaine d'application) dans le bon gestionnaire de context !
    """
    with app.app_context():
        from . import auth, main
        app.register_blueprint(auth.auth_blueprint)
        app.register_blueprint(main.main_blueprint)

    return app


app = create_app()


# Pour initialiser la bdd app.bd
import myapp.models
@app.cli.command("init_db_test") # Très important, ne pas oublié de passer "init_db" en paramètre au décorateur
def init_db_test():
    models.init_db()

# Pour incorporer le fichier de test (qui comprend les premières affaires)
@app.cli.command("ajout_fichier_csv_test")
def ajout_fichier_csv_test():
    models.ajout_fichier_csv()

