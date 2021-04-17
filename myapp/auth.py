# coding:utf-8

"""
Ensemble des routes pour l'authentification
"""

from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user, login_user
from . import form
from .models import User

# Blueprint
auth_blueprint = Blueprint('auth_blueprint', __name__, url_prefix='/auth')

@auth_blueprint.route('/', methods=['GET', 'POST']) #renvoie vers /auth
def auth():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    formulaire = form.LoginForm()
    if formulaire.validate_on_submit():
        user = User.query.filter_by(username=formulaire.username.data).first()
        if user is None or not user.check_password(formulaire.password.data):
            flash('Utilisateur ou mot de passe invalide')
            redirect(url_for('auth_blueprint.auth'))
        login_user(user, remember=formulaire.remember_me.data)
        return redirect(url_for('main_blueprint.index'))
    return render_template('auth.html', title="Login", form=formulaire)

