# Importer la classe performance
# Importer la classe croisement
from Coordonnee import Coordonnee

class Individu:
    def __init__(self, coordonnees):
        self.coordonnees = coordonnees # nom des variables, liste des valeurs, codage en base prédéfinie
        self.scorePerformance = None # evaluation de la fonction choisie # l'objet

    def set_score_performance(self, population):
        self.scorePerformance = population.fonctionPerformance.eval([coord.valeur for coord in self.coordonnees])