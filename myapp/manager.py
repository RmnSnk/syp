# coding:utf-8

""""
Blueprint de la partie manager
"""

from flask import Blueprint, render_template, flash, redirect, url_for
from .models import User
from . import form
from . import db
from datetime import datetime
from flask_login import login_required

# Blueprint
manager_blueprint = Blueprint('manager_blueprint', __name__, url_prefix='/manager')

@manager_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def manager():
    formulaire = form.RegistrationForm()
    if formulaire.validate_on_submit():
        user = User(email=formulaire.email.data, dgi=formulaire.dgi.data, manager=formulaire.manager.data, active=True)
        user.set_password(formulaire.password.data)
        user.set_username(formulaire.email.data)
        db.session.add(user)
        db.session.commit()
        flash("Utilisateur crée")
        return redirect(url_for('main_blueprint.index'))
    return render_template('manager.html', title="Espace manager", form=formulaire)