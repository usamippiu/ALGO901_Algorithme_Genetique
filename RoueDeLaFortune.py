import random
import math

from Selection import Selection
from Individu import Individu
from Coordonnee import Coordonnee
from Fenetre import Fenetre
from CodageBinaire import CodageBinaire
from Population import population


# Avec cette méthode, chaque valeur d'une fonction occupe une certaine proportion de la roue.
# Il s'agit de tirer des valeurs (individus) en fonction de la proportion d'occupation de la roue.
# On calcule la performance totale (total_performance) de l'ensemble des évaluations des valeurs par la fonction.
# Chaque individu a une proportion d'occupation de la roue (valeur/total_performance).
# On tire un nombre aléatoirement.
# On regarde si l'évaluation de l'individu par la fonction est supérieure au nombre aléatoire.
# Cela permet de choisir suivant des proportions d'occupation de la roue.

class RoueDeLaFortune(Selection):
    def __init__(self, population):
        super().__init__(population)

    def calculeTotalPerformance(self):
        total_perf = sum(scoreperformance for scoreperformance in self.population.individu.scorePerfomance) # somme le score de performance de tout les individus de la population en paramètre de l'objet RoueDeLaFortune
        return total_perf

    def roue_de_la_fortune(self):
        total_performance = self.calculeTotalPerformance()

        # Tirage d'un nombre aléatoire entre 0 et total_performance
        nombreAlea = random.uniform(0, total_performance)

        # Parcours de la population et sélection de l'individu choisi
        perf = 0
        for individu in self.population.individus:
            # calcul de la performance de l'individu (évaluation par la fonction)
            perf += self.population.individu.scorePerformance

            # comparaison de l'évaluation avec le nombre aléatoire tiré initialement :
            # si sa valeur est supérieure ou égale au nombre, on le retourne
            if perf >= nombreAlea:
                return individu


    def selection_parents(self):
        total_performance = self.calculeTotalPerformance()

        parent1 = self.roue_de_la_fortune()
        parent2 = self.roue_de_la_fortune()

        while parent1 == parent2:
            parent2 = self.roue_de_la_fortune()

        return parent1, parent2
    

if __name__=="__main__":
    def f(x):
        return x**2

    def g(x):
        return math.sqrt(x)
    
    fenetreX = Fenetre(-10,10,'x')
    codage = CodageBinaire([32,6])
    coordonneeX1 = Coordonnee(1, fenetreX, codage)
    x1 = Individu(coordonneeX1)
    coordonneeX2 = Coordonnee(2, fenetreX, codage)
    x2 = Individu(coordonneeX2)
    coordonneeX3 = Coordonnee(3, fenetreX, codage)
    x3 = Individu(coordonneeX3)
    coordonneeX4 = Coordonnee(4, fenetreX, codage)
    x4 = Individu(coordonneeX4)
    coordonneeX5 = Coordonnee(5, fenetreX, codage)
    x5 = Individu(coordonneeX5)

    population = population([x1,x2,x3,x4,x5], f)

    methode = RoueDeLaFortune(population)
    print(methode.calculeTotalPerformance())

    print(methode.selection_parents())