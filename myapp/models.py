
from datetime import datetime
import logging as lg
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


from . import db, login
from .utils_csv import *

""" Partie relative à la table Affaire qui stocke les affaires"""

class Affaire(db.Model):

    # Ces informations vont permettre de créer la table 'Affaire'

    numero = db.Column(db.Integer, primary_key=True) # Numéro Illiad
    dossier = db.Column(db.String) # Nom contribuable
    adresse = db.Column(db.String) # Adresse Contribuable
    date_demande = db.Column(db.Date) # Date de la demande
    agent_id = db.Column(db.Integer, db.ForeignKey('user.id')) # Agent qui traite le dossier table user, champ id
    etat = db.Column(db.Boolean) # False : non traité, True : traité


    # Remarque : même en l'absence de constructeur, id, fullname et nickname sont accessible de puis User.id, User.nickname...
    def __init__(self, dict_affaire):
        self.numero = dict_affaire['N°']
        self.dossier = dict_affaire['Dossier']
        self.adresse = dict_affaire['Adresse']
        self.date_demande = (datetime.strptime(dict_affaire['Date demande'], "%d/%m/%Y")).date()
        self.agent_id = None
        self.etat = False

    def __repr__(self):
        return f"Affaire {self.numero} | Contribuable {self.dossier}"


class ListeToBdd:

    """
    :param liste: une liste contenant un ensemble de dictionnaire
    :return: Voir si on doit pas retourner 1 ou 0 en fonction d'un try pour voir si sa marche ou pas
    """

    def __init__(self, liste):
        self.liste = liste

    def importationDansLaBdd(self):

        for dico in self.liste: # dico est un dictionnaire qui contient une ligne du fichier CSV
            affaire = Affaire(dico)
            db.session.add(affaire)
            db.session.commit()

def ajout_fichier_csv():
    csv = Cvs_import(PATHTOCSVFILELATIN)
    csv.csvToObject()

    # csv.pythonObject contient notre liste de dictionnaire que l'on doit importer
    listeToBdd = ListeToBdd(csv.pythonObject)
    listeToBdd.importationDansLaBdd()
    lg.warning('Fichier importé')


""" Partie relative à la table User qui gère les utilisateurs """

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dgi = db.Column(db.Integer, unique=True)
    email = db.Column(db.String(64), unique=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    manager = db.Column(db.Boolean) # True : manager, False : agent
    active = db.Column(db.Boolean) # True : actif, False : inactif
    affaire = db.relationship('Affaire', backref='agent', lazy='dynamic')

    def __repr__(self):
        return f"Utilisateur  {self.username}"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def set_username(self, email):
        l = email.split('@')
        self.username = l[0]


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


""" Création des tables """

def init_db():
    db.drop_all()
    db.create_all()
    lg.warning('Database Affaires and User initialized')



