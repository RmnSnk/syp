# coding:utf-8

""""
Blueprint de la partie agent
"""

from flask import Blueprint, render_template, url_for
from .models import Affaire
from datetime import datetime
from flask_login import login_required

# Blueprint
agent_blueprint = Blueprint('agent_blueprint', __name__, url_prefix='/agent')

@agent_blueprint.route('/')
@login_required
def mes_affaires():
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
        l.append(aff.agent_id)
        l.append(aff.date_demande)
        liste_aff.append(l)
    return render_template('mes_affaires.html', title="Espace agent", liste_affaires=liste_aff)