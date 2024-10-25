import random
import math

from Selection import Selection
from Individu import Individu
from Coordonnee import Coordonnee
from Fenetre import Fenetre
from CodageBinaire import CodageBinaire


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
        #self.performance = performance

    def calculeTotalPerformance(self):

        total_performance = sum(self.performance(individu) for individu in self.population)
        return total_performance

    def roueDeLaFortune(self):
        total_performance = self.calculeTotalPerformance()

        # Tirage d'un nombre aléatoire entre 0 et total_performance
        nombreAlea = random.uniform(0, total_performance)

        # Parcours de la population et sélection de l'individu choisi
        perf = 0
        for individu in self.population.individu:
            # calcul de la performance de l'individu (évaluation par la fonction)
            perf += self.population.individu.performance

            # comparaison de l'évaluation avec le nombre aléatoire tiré initialement :
            # si sa valeur est supérieure ou égale au nombre, on le retourne
            if perf >= nombreAlea:
                return individu


    def selectionParents(self):
        total_performance = self.calculeTotalPerformance()

        parent1 = self.roueDeLaFortune()
        parent2 = self.roueDeLaFortune()

        while parent1 == parent2:
            parent2 = self.roueDeLaFortune()

        return parent1, parent2
    

if __name__=="__main__":
    def f(x):
        return x**2

    def g(x):
        return math.sqrt(x)
    
    fenetreX = Fenetre(-10,10,'x')
    codage = CodageBinaire()
    coordonneeX1 = Coordonnee(1, fenetreX, codage)
    x1 = Individu(coordonneeX1, f)
    coordonneeX2 = Coordonnee(2, fenetreX, codage)
    x2 = Individu(coordonneeX2, f)
    coordonneeX3 = Coordonnee(3, fenetreX, codage)
    x3 = Individu(coordonneeX3, f)
    coordonneeX4 = Coordonnee(4, fenetreX, codage)
    x4 = Individu(coordonneeX4, f)
    coordonneeX5 = Coordonnee(5, fenetreX, codage)
    x5 = Individu(coordonneeX5, f)

    population = [x1,x2,x3,x4,x5]

    methode = RoueDeLaFortune(population)
    print(methode.calculeTotalPerformance())

    print(methode.selectionParents())