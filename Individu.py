# Importer la classe performance
# Importer la classe croisement
from Coordonnee import Coordonnee


class Individu:
    def __init__(self, coordonnees):
        self.coordonnees = coordonnees  # nom des variables, liste des valeurs, codage en base prédéfinie
        self.score_performance = None  # evaluation de la fonction choisie # l'objet

    def set_score_performance(self, population):
        self.score_performance = population.fonction_performance.eval(
            [coord.valeur for coord in self.coordonnees]
        )
