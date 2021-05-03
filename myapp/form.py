# coding:utf-8

"""
Formulaires du site
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from .models import User

class LoginForm(FlaskForm):
    username = StringField('Utilisateur', validators=[DataRequired()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    remember_me = BooleanField('Se souvenir de moi ?')
    submit = SubmitField('Se connecter')

class RegistrationForm(FlaskForm):
    """
    TODO: modifier pour n'avoir qu'à saisir le début de l'adresse mail
    TODO: modifier pour créer un mot de passe automatique envoyé par mail
    """
    dgi = IntegerField('Numéro DGI', validators=[DataRequired()])
    email = StringField('Email Professionnel', validators=[DataRequired(), Email()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    password2 = PasswordField('Confirmez le mot de passe', validators=[DataRequired(), EqualTo('password')])
    manager = BooleanField('Créer un manager')
    submit = SubmitField('Créer l\'utilisateur')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Cet utilisateur existe déjà')
        l = email.data.split('@')
        if l[1] != 'dgfip.finances.gouv.fr':
            raise ValidationError('L\'adresse email doit se terminer par @dgfip.finances.gouv.fr')

    def validate_dgi(self, dgi):
        if len(str(dgi.data)) != 6:
            raise ValidationError('Le numéro DGI doit faire exactement 6 chiffes')
        user = User.query.filter_by(dgi=dgi.data).first()
        if user is not None:
            raise ValidationError('Ce numéro a déjà été utilisé')

class DeleteForm(FlaskForm):

    agent = SelectField('Choisir l\'utilisateur à supprimer', choices=["1", "2"])
    submit = SubmitField('Supprimer l\'utilisateur')

    #TODO : Remplacer les possibilité agent / choice= .... par une liste d'agent
    #TODO : Cette liste d'agent pourra prendre la forme d'un tupple (id, nom)
    #TODO : Le champs de rechercher indiquera le nom mais reverra l'id

        #TODO : faire recherche sur la base et renvoyer une liste qui contient tout les username
