# coding:utf-8

"""
Blueprint de l'application principale : index, contact, aide ...
"""

from flask import Blueprint, render_template, url_for
from .models import Affaire
from datetime import datetime

# Blueprint
main_blueprint = Blueprint('main_blueprint', __name__, url_prefix='/')

@main_blueprint.route('/') #renvoie vers /
@main_blueprint.route('/index')
def index():

    requete = Affaire.query.order_by(Affaire.date_demande)
    liste_aff = []
    for aff in requete:
        l = []
        l.append(aff.numero)
        l.append(aff.dossier)
        l.append(aff.adresse)
        # Lorque l'on soustrait 2 date, le résultat est un objet timedelta qui est donné en jour, minute, secondes
        # La methode .days permet de ne garder que les jours
        l.append((datetime.today().date() - aff.date_demande).days)
        l.append(aff.agent)
        l.append(aff.date_demande)
        liste_aff.append(l)


    return render_template('index.html',title="Bienvenue", liste_affaires=liste_aff)

