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
    liste_username = form.liste_users()
    formulaire_deluser.agent.choices = liste_username

    if formulaire_deluser.validate_on_submit():
        user = User.query.filter_by(username=formulaire_deluser.agent.data).first()
        db.session.delete(user)
        db.session.commit()
        flash("Utilisateur supprimé")
        return redirect(url_for('main_blueprint.index'))
    return render_template('manager_delete.html', title="Espace manager", form=formulaire_deluser)

@manager_blueprint.route('modify', methods=['GET', 'POST'])
@login_required
def manager_modify():
    formulaire_moduser = form.ModifyForm()
    liste_username = form.liste_users()
    formulaire_moduser.agent.choices = liste_username

    if formulaire_moduser.validate_on_submit():
        user = User.query.filter_by(username=formulaire_moduser.agent.data).first()
        user.dgi = formulaire_moduser.dgi.data
        user.manager = formulaire_moduser.manager.data
        user.active = formulaire_moduser.active.data

        user.set_password(formulaire_moduser.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Utilisateur modifié")
        return redirect(url_for('main_blueprint.index'))
    return render_template('manager_modify.html', title="Espace manager", form=formulaire_moduser)
