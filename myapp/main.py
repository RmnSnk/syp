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


@main_blueprint.route('/test')
def test():
    return "Test"