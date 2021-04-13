# coding:utf-8

"""
Fichier de configuration global
"""

import os

# Le chemin d'accès de répertoire de l'application (~/PycharmProjects/syp_migration)
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    # Secret Key
    SECRET_KEY = "dev"

    # Paramètres pour Flask_SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_ECHO = True # Pour avoir l'affichage des requetes
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Pour enlever le warning au lancement de l'application

    # Variables personnelles
    TEST_CSV_PATH = os.path.join(basedir, 'myapp/static/files/test_fichier.csv')
    BASEDIR = basedir