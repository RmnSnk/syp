# coding:utf-8

"""
Ensemble des routes pour l'authentification
"""

from flask import Blueprint, render_template, flash, redirect, url_for
from . import form

# Blueprint
auth_blueprint = Blueprint('auth_blueprint', __name__, url_prefix='/auth')

@auth_blueprint.route('/', methods=['GET', 'POST']) #renvoie vers /auth
def auth():
    formulaire = form.LoginForm()
    if formulaire.validate_on_submit():
        flash(f"Identifiant envoyés pour l'utilsateur {formulaire.username.data}, Se_souvenir : {formulaire.remember_me.data}")
        return redirect('/index')
    return render_template('auth.html',title="Login", form=formulaire)

