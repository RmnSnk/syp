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

@manager_blueprint.route('create', methods=['GET', 'POST'])
@login_required
def manager_create():
    formulaire_newuser = form.RegistrationForm()
    if formulaire_newuser.validate_on_submit():
        user = User(email=formulaire_newuser.email.data, dgi=formulaire_newuser.dgi.data, manager=formulaire_newuser.manager.data, active=True)
        user.set_password(formulaire_newuser.password.data)
        user.set_username(formulaire_newuser.email.data)
        db.session.add(user)
        db.session.commit()
        flash("Utilisateur crée")
        return redirect(url_for('main_blueprint.index'))
    return render_template('manager_create.html', title="Espace manager", form=formulaire_newuser)


@manager_blueprint.route('delete', methods=['GET', 'POST'])
@login_required
def manager_delete():
    formulaire_deluser = form.DeleteForm()

    if formulaire_deluser.validate_on_submit():
        user = User.query.filter_by(username=formulaire_deluser.agent.data).first()
        db.session.delete(user)
        db.session.commit()
        flash("Utilisateur supprimé")
    return render_template('manager_delete.html', title="Espace manager", form=formulaire_deluser)