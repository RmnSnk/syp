# coding:utf-8

"""
Ensemble des routes pour l'authentification
"""

from flask import Blueprint
from myapp import db

# Blueprint
auth_blueprint = Blueprint('auth_blueprint', __name__, url_prefix='/auth')

@auth_blueprint.route('/') #renvoie vers /bprint
def bprint():
    return '<h1>Test avec Blueprint</h1>'

