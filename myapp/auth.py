# coding:utf-8

"""
Ensemble des routes pour l'authentification
"""

from flask import Blueprint, render_template
from . import form

# Blueprint
auth_blueprint = Blueprint('auth_blueprint', __name__, url_prefix='/auth')

@auth_blueprint.route('/') #renvoie vers /auth
def auth():
    formulaire = form.LoginForm()
    return render_template('auth.html', form=formulaire)

