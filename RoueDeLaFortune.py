import random

from SelectionParents import SelectionParents as Selection
from Individu import Individu
from Coordonnee import Coordonnee
from Fenetre import Fenetre
from CodageBinaire import CodageBinaire
from Population import Population
from Carre import F


# Cette méthode de sélection consiste à tirer des individus pour minimiser une fonction.
# On tire une valeur cible aléatoirement entre 0 et la somme des performances ;
# on initialise une variable perf = 0 qui sert de compteur cumulatif des performances de chaque individu :
# on l'initialise à 0 car on veut calculer la contribution de chaque individu à partir de 0 ;
# elle calcule la somme des inverses des valeurs de performances (pour minimiser la fonction), jusqu'à atteindre la valeur cible ;
# on sélectionne l'individu qui vérifie cette condition.
# Ainsi, chaque individu occupe une proportion de la roue, proportionnellement à son score de performance.
# Atteindre la valeur cible signifie qu'on a trouvé l'individu sélectionné.


class RoueDeLaFortune(Selection):

    def calcule_total_performance(self, population, offset):
        total_perf = sum(
            1 / (individu.scorePerformance + offset + 1e-9)
            for individu in population.individus
        )
        return total_perf

    """def calcule_total_performance(self):
        min_fitness = min(individu.scorePerformance for individu in self.population.individus)
        offset = abs(min_fitness) + 1e-9  # Décalage pour rendre toutes les valeurs positives
        total_perf = sum(1/score for score in [individu.scorePerformance + offset for individu in self.population.individus])
        return total_perf"""

    """def ajuste_fitness(self):
        min_fitness = min(
            individu.scorePerformance for individu in self.population.individus
        )
        offset = (
            abs(min_fitness) + 1e-9
        )  # Décalage pour rendre toutes les valeurs positives
        return [
            individu.scorePerformance + offset for individu in self.population.individus
        ]"""

    def get_offset(self, population):
        return abs(
            min(
                0,
                min(individu.scorePerformance for individu in population.individus),
            )
        )

    def roue_de_la_fortune(self, population):
        # Calcul de la performance totale
        offset = self.get_offset(population)
        total_performance = self.calcule_total_performance(population, offset)

        # Tirage d'un nombre aléatoire entre 0 et la somme totale des performances en valeur absolue
        valeurAleatoire = random.uniform(0, abs(total_performance))

        # Parcours de la population et sélection de l'individu correspondant
        perf = 0
        scoreIndividu = 0
        for individu in population.individus:
            # On utilise l'inverse de la fonction pour minimiser : les proportions les plus faibles deviennent les plus grandes
            # print("score =", individu.scorePerformance)
            perf += 1 / (individu.scorePerformance + offset + 1e-9)
            if perf >= valeurAleatoire:
                return individu, perf

    def selection_parents(self, population):

        parent1 = self.roue_de_la_fortune(population)
        parent2 = self.roue_de_la_fortune(population)

        while parent1 == parent2:
            parent2 = self.roue_de_la_fortune(population)

        return parent1, parent2

    def selection_n_individus(self, population):

        # initialisation de la population de sortie
        population_sortie = []

        for i in range(population.nombreMax):
            # selection d'un premier individu parmi la population
            individu_1 = self.roue_de_la_fortune(population)[0]
            # on enlève l'individu de la population initiale et on l'ajoute à la population de sortie
            population.individus.remove(individu_1)
            population_sortie.append(individu_1)

        return Population(
            population.nombreMax,
            population.fonctionPerformance,
            population_sortie,
        )


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
    coordonneeX2 = Coordonnee(fenetreX, codage, 2)
    x2 = Individu([coordonneeX2])
    # x2.scorePerformance = f.eval(2)
    coordonneeX3 = Coordonnee(fenetreX, codage, 3)
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

    # ajout des individus dans la population
    population1.ajouter_individus([x11, x21, x31])
    print(len(population1.individus))

    # population_fusionnée
    population_fusion = Population(
        population.nombreMax,
        population.fonctionPerformance,
        population.individus + population1.individus,
    )

    print("type = ", type(population_fusion))

    methode = RoueDeLaFortune()
    print(
        "performance totale = ",
        methode.calcule_total_performance(population, methode.get_offset(population)),
    )
    listeParents = methode.selection_parents(population)
    print([parent[0].coordonnees[0].valeur for parent in listeParents])

    methode1 = RoueDeLaFortune()
    nouvelle_population = methode1.selection_n_individus(population_fusion)
    print([parent.coordonnees[0].valeur for parent in nouvelle_population.individus])
