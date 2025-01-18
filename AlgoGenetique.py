from Fenetre import Fenetre
from Population import Population
from RoueDeLaFortune import RoueDeLaFortune
from Tournoi import Tournoi
from CodageBinaire import CodageBinaire
from CodageHexadecimal import CodageHexadecimal
from Carre import F
from Schwefel import Schwefel
from F2 import F2
from F6 import F6
from F7 import F7
from F8 import F8
from F9 import F9
from SixHumpCamelSix import SixHumpCamelSix
from CroisementSimple import CroisementSimple
import numpy as np


class AlgoGenetique:
    def __init__(
        self,
        fonction,
        ranges,
        taille_population,
        nb_iter_max,
        codage,
        selection,
        croisement,
    ):
        self.fonction = fonction
        self.nb_iter_max = nb_iter_max
        self.taille_population = taille_population
        self.fenetres = []
        for i in range(len(ranges)):
            self.fenetres.append(Fenetre(f"x{i}", ranges[i][0], ranges[i][1]))
        self.codage = codage
        self.population = Population(self.taille_population, self.fonction)
        self.selection = selection
        self.croisement = croisement

        self.population.generer_population(self.fenetres, self.codage)
        self.individu_min = self.population.lf_individu_minimal()

    def get_min(self):
        for nb_iter in range(self.nb_iter_max):
            # Pour la selection des parents on copie avant
            population_copy = self.population.copy()

            # Construction des couples
            couples = []

            while len(population_copy.individus) > 1:
                [parent1, parent2] = self.selection.selection_parents(population_copy)
                population_copy.supprimer_individus([parent1, parent2])
                couples.append([parent1, parent2])

            # Construction des enfants
            enfants = []
            for couple in couples:
                enfants_couple = np.array(
                    self.croisement.perform_crossover(couple[0], couple[1])
                )
                np.random.shuffle(enfants_couple)

                enfants += [enfants_couple[0], enfants_couple[1]]

            # Check min avant de changer de pop
            if (
                self.individu_min.score_performance
                > self.population.lf_individu_minimal().score_performance
            ):
                self.individu_min = self.population.lf_individu_minimal()

            # Selection prochaine generation
            self.population.ajouter_individus(enfants)
            self.selection.selection_n_individus(
                self.population, (self.population.nombre_max)
            )

        return [
            coordonnee.valeur for coordonnee in self.individu_min.coordonnees
        ], self.individu_min.score_performance


if __name__ == "__main__":
    """
    alg = AlgoGenetique(
        Schwefel(),
        [[0, 500], [0, 500]],
        50,
        100,
        CodageBinaire([52, 10]),
        RoueDeLaFortune(),
        CroisementSimple(),
    )
    res, value = alg.get_min()
    print(res[0], res[1], value)
    """

    """
    alg = AlgoGenetique(
        SixHumpCamelSix(),
        [[-5, 5], [-5, 5]],
        200,
        500,
        CodageBinaire([52, 10]),
        RoueDeLaFortune(),
        CroisementSimple(),
    )
    res, value = alg.get_min()
    print(res[0], res[1], value)
    """
    """
    alg = AlgoGenetique(
        F2(),
        [[-2.048, 2.048], [-2.048, 2.048]],
        100,
        100,
        CodageBinaire([52, 10]),
        RoueDeLaFortune(),
        CroisementSimple(),
    )
    res, value = alg.get_min()
    print(res[0], res[1], value)"""
    """
    alg = AlgoGenetique(
        F6(),
        [[-100, 100], [-100, 100]],
        100,
        100,
        CodageHexadecimal([52, 10]),
        RoueDeLaFortune(),
        CroisementSimple(),
    )
    res, value = alg.get_min()
    print(res[0], res[1], value)
    """

    """alg = AlgoGenetique(
        F7(),
        [
            [-5.12, 5.12],
            [-5.12, 5.12],
            [-5.12, 5.12],
            [-5.12, 5.12],
            [-5.12, 5.12],
            [-5.12, 5.12],
            [-5.12, 5.12],
            [-5.12, 5.12],
            [-5.12, 5.12],
            [-5.12, 5.12],
        ],
        100,
        100,
        CodageBinaire([52, 10]),
        RoueDeLaFortune(),
        CroisementSimple(),
    )
    res, value = alg.get_min()
    print(res[0], res[1], value)"""

    """alg = AlgoGenetique(
        F8(),
        [
            [-600, 600],
            [-600, 600],
            [-600, 600],
            [-600, 600],
            [-600, 600],
            [-600, 600],
            [-600, 600],
            [-600, 600],
            [-600, 600],
            [-600, 600],
        ],
        100,
        100,
        CodageHexadecimal([52, 10]),
        RoueDeLaFortune(),
        CroisementSimple(),
    )
    res, value = alg.get_min()
    print(res[0], res[1], value)"""

    alg = AlgoGenetique(
        F9(),
        [
            [-500, 500],
            [-500, 500],
            [-500, 500],
            [-500, 500],
            [-500, 500],
            [-500, 500],
            [-500, 500],
            [-500, 500],
            [-500, 500],
            [-500, 500],
        ],
        100,
        100,
        CodageBinaire([52, 10]),
        RoueDeLaFortune(),
        CroisementSimple(),
    )
    res, value = alg.get_min()
    print(res[0], res[1], value)
