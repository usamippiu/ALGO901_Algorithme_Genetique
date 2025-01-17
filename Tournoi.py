from Selection import Selection
from Individu import Individu
from Coordonnee import Coordonnee
from CodageBinaire import CodageBinaire
from Fenetre import Fenetre
from Carre import F
from Population import Population

import numpy as np


class Tournoi(Selection):
    def __init__(self, p):
        self.p = p

    def tournoi(self, individus):
        individus_sorted = sorted(
            [individu for individu in individus],
            key=lambda x: x.score_performance,
        )
        weights = np.array(
            [self.p * (1 - self.p) ** i for i in range(len(individus_sorted))]
        )

        return np.random.choice(individus, p=weights / sum(weights))

    def selection_n_indivs(self, population, n):
        individus = population.individus.copy()
        n_individus = []
        for i in range(n):
            individu = self.tournoi(individus)
            n_individus.append(individu)
            individus.remove(individu)

        return n_individus

    def selection_parents(self, population):
        return self.selection_n_indivs(population, 2)

    def selection_n_individus(self, population, n):
        population.individus = self.selection_n_indivs(population, n)


if __name__ == "__main__":
    # choix de la fonction carré à une variable
    f = F()

    # initialisation de la fenetre
    fenetreX = Fenetre(-10, 10, "x")

    # choix du codage
    codage = CodageBinaire([32, 6])

    # initialisation des coordonnees et des individus
    coordonneeX1 = Coordonnee(fenetreX, codage, 1)
    x1 = Individu([coordonneeX1])
    # x1.scorePerformance = f.eval(1)
    coordonneeX2 = Coordonnee(fenetreX, codage, 5)
    x2 = Individu([coordonneeX2])
    # x2.scorePerformance = f.eval(2)
    coordonneeX3 = Coordonnee(fenetreX, codage, 10)
    x3 = Individu([coordonneeX3])

    # initialisation de la population
    population = Population(3, f)

    # ajout des individus dans la population
    population.ajouter_individus([x1, x2, x3])

    # initialisation des coordonnees et des individus
    coordonneeX11 = Coordonnee(fenetreX, codage, -2)
    x11 = Individu([coordonneeX11])
    # x1.scorePerformance = f.eval(1)
    coordonneeX21 = Coordonnee(fenetreX, codage, -1)
    x21 = Individu([coordonneeX21])
    # x2.scorePerformance = f.eval(2)
    coordonneeX31 = Coordonnee(fenetreX, codage, 2.5)
    x31 = Individu([coordonneeX31])

    # initialisation de la population
    population1 = Population(3, f)

    tournoi = Tournoi(0.5)
    tournoi.selection_n_individus(population, 2)
    print([individu.coordonnees[0].valeur for individu in population.individus])
