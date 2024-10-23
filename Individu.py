# Importer la classe coordonnées
# Importer la classe performance
# Importer la classe croisement
from Coordonnees import Coordonnees

class Individu:
    def __init__(self, coordonnees, performance):
        self.coordonnees = coordonnees # nom des variables, liste des valeurs, codage en base prédéfinie
        self.performance = performance # evaluation de la fonction choisie

    # getCodage
    # getCoords
    # appeler self.codageBaseX.code(individu) pour remplir cet attribut
    # code(Individu) -> lit les coordonnees d'un individu et les converti au bon format