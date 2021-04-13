
from datetime import datetime
import logging as lg

from . import db
from .utils_csv import *

""" Partie relative à la table Affaire qui stocke les affaires"""

class Affaire(db.Model):

    # Ces informations vont permettre de créer la table 'Affaire'

    numero = db.Column(db.Integer, primary_key=True) # Numéro Illiad
    dossier = db.Column(db.String) # Nom contribuable
    adresse = db.Column(db.String) # Adresse Contribuable
    date_demande = db.Column(db.Date) # Date de la demande
    agent = db.Column(db.String) # Agent qui traite le dossier
    etat = db.Column(db.Boolean) # False : non traité, True : traité


    # Remarque : même en l'absence de constructeur, id, fullname et nickname sont accessible de puis User.id, User.nickname...
    def __init__(self, dict_affaire):
        self.numero = dict_affaire['N°']
        self.dossier = dict_affaire['Dossier']
        self.adresse = dict_affaire['Adresse']
        self.date_demande = (datetime.strptime(dict_affaire['Date demande'], "%d/%m/%Y")).date()
        self.agent = None
        self.etat = False


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

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # TODO : Pour le moment un entier qui incrémente, remplacer par le numéro DGI
    username = db.Column(db.String(64), index=True, unique=True)
    email= db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f"Utilisateur  {self.username}"


""" Création des tables """

def init_db():
    db.drop_all()
    db.create_all()
    lg.warning('Database initialized')



