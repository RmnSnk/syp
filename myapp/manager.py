# coding:utf-8

""""
Blueprint de la partie manager
"""

from flask import Blueprint, render_template, url_for
from .models import Affaire
from datetime import datetime
from flask_login import login_required

# Blueprint
manager_blueprint = Blueprint('manager_blueprint', __name__, url_prefix='/manager')

@manager_blueprint.route('/')
@login_required
def manager():
    return url_for('manager.html')