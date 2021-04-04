# coding: utf-8

# Notre module de CSV
from csv import DictReader
from flask import current_app
import os

# Voir si ça marche lorsque l'application tourne

"""
On utilise ici current_app pour accéder à la configuration, en effet app n'est pas encore terminée d'être contruite !
voir le note dans l'usine à application de __ini__.py
"""
PATHTOCSVFILELATIN = current_app.config['TEST_CSV_PATH']
PATHTOCSVFILEUTF8 = os.path.join(current_app.config['BASEDIR'], 'myapp/static/temp/utf8.csv')


class Cvs_import(object):

    """
    Permet d'obtenir l'attribut pythonObject qui est une liste qui contient des dictionnaire.
    Chaque dictionnaire contient une ligne du fichier CVS (encodé en UTF8). Les clé du dictionnaire sont les colonnes
    du fichier CSV.

    """

    def __init__(self, f_csv):
        self.f_csv = f_csv # contient un str avec le chemin du fichier CVS latin3 lors de l'initialisation. Puis après csvToUtf8, contient le chemin du fichier utf8
        self.f_csv_utf8 = PATHTOCSVFILEUTF8
        self.pythonObject = []

    def csvToObject(self):

        """
        :return: Une liste contenant autant des dictionnaire que de lignes du fichier CVS encondées en utf8. Les clés des dictionnaires sont les intitulés de colonnes.

        """

        # Etape 1 : on réencode en utf8 nos données. On crée un nouveau fichie utf8.csv pour les stocker
        with open(self.f_csv, 'r', encoding='latin3', newline='') as csvLatin3:
            r = csvLatin3.read()
            for rows in r:
                # Le nouveau fichier se nomme "utf8.csv", il se trouve dans static/temp
                with open(self.f_csv_utf8, 'a', encoding="utf-8", newline='') as cvsUtf8:
                    cvsUtf8.write(rows)

        # Etape 2 : On va maintenant transformer les données contenues dans le cvs (utf8) en objet python (en une liste contenant des dictionnaires)
        # Les clés de ces dictionnaires sont les intitulées des colonnes du fichier CVS

        with open(self.f_csv_utf8, encoding='utf-8', newline='') as csvfile:
            r = DictReader(csvfile)
            for row in r:
                self.pythonObject.append(row)

        # On efface le fichier utf8.csv (dans static/temp)
        os.remove(PATHTOCSVFILEUTF8)
