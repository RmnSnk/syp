# coding:utf-8

"""
Formulaires du site
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
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
    username = StringField('Utilisateur', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    numero_dgi = IntegerField('Numéro DGI', validators=[DataRequired()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    password2 = PasswordField('Confirmez le mot de passe', validators=[DataRequired(), EqualTo('password')])
    manager = BooleanField('Créer un compte manager ?')
    submit = SubmitField('Créer l\'utilisateur')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Merci de saisir un autre nom d\'utilisateur')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.date).first()
        if user is not None:
            raise ValidationError('Merci de saisir une adresse email différente')