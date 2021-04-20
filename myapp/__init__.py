# coding:utf-8

"""
Usine à application

https://hackersandslackers.com/flask-application-factory/

"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config



# On créer les objets vides
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)      # Configuration de base de l'application dans l'objet config
    app.config.from_pyfile('config.py') # Configuration particulières de l'instance

    # On instancie les objets
    db.init_app(app) # + db = -> equivaut à db = SQLAlchemy(app)
    migrate.init_app(app, db) # + migrate -> equivaut à migrate = Migrate(app, db)
    login.init_app(app) # idem
    login.login_view = 'auth_blueprint.auth'

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
        from . import auth, main, agent, manager
        app.register_blueprint(auth.auth_blueprint)
        app.register_blueprint(main.main_blueprint)
        app.register_blueprint(agent.agent_blueprint)
        app.register_blueprint(manager.manager_blueprint)

    return app


app = create_app()


# Pour initialiser la bdd app.bd
import myapp.models
@app.cli.command("init_db") # Très important, ne pas oublié de passer "init_db" en paramètre au décorateur
def init_db():
    models.init_db()

# Pour incorporer le fichier de test (qui comprend les premières affaires)
@app.cli.command("ajout_fichier_csv")
def ajout_fichier_csv():
    models.ajout_fichier_csv()

from .models import Affaire, User # Placé ici pour éviter les dépendances circulaires

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Affaire': Affaire}

