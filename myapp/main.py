# coding:utf-8

"""
Blueprint de l'application principale : index, contact, aide ...
"""

from flask import Blueprint, render_template, url_for
from .models import Affaire
from datetime import datetime
from flask_login import login_required

# Blueprint
main_blueprint = Blueprint('main_blueprint', __name__, url_prefix='/')

@main_blueprint.route('/') #renvoie vers /
@main_blueprint.route('/index')
def index():
    return render_template('index.html')



@main_blueprint.route('/mes_affaires')
@login_required
def mes_affaires():
    liste_aff = []
    for aff in requete:
        l = []
        l.append(aff.numero)
        l.append(aff.dossier)
        l.append(aff.adresse)
        # Lorque l'on soustrait 2 date, le résultat est un objet timedelta qui est donné en jour, minute, secondes
        # La methode .days permet de ne garder que les jours
        l.append((datetime.today().date() - aff.date_demande).days)
        l.append(aff.agent_id)
        l.append(aff.date_demande)
        liste_aff.append(l)
    return render_template('mes_affaires.html',title="Bienvenue", liste_affaires=liste_aff)

@main_blueprint.route('/test')
def test():
    return "Test"