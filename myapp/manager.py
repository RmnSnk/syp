# coding:utf-8

""""
Blueprint de la partie manager
"""

from flask import Blueprint, render_template, flash, redirect, url_for
from .models import User
from .form import RegistrationForm
from . import db
from datetime import datetime
from flask_login import login_required

# Blueprint
manager_blueprint = Blueprint('manager_blueprint', __name__, url_prefix='/manager')

@manager_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def manager():
    formulaire = RegistrationForm()
    if formulaire.validate_on_submit():
        user = User(username=formulaire.username.data, email=formulaire.email.data)
        user.set_password(formulaire.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Utilisateur crée")
        return redirect(url_for('main_blueprint.index'))

    return render_template('manager.html', title="Espace manager", form=formulaire)