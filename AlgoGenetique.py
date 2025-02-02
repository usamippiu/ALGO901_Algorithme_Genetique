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
from CroisementDouble import CroisementDouble
from MutationParPermutation import MutationParPermutation
from MutationParFlipping import MutationParFlipping
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
        mutation,
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
        self.mutation = mutation

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

            # Mutations

            self.mutation.effectuer_mutation(self.population)

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

    """alg = AlgoGenetique(
        Schwefel(),
        [[-500, 500], [-500, 500]],
        100,
        500,
        CodageBinaire([52, 10]),
        RoueDeLaFortune(),
        CroisementDouble(),
        MutationParPermutation(0.1),
    )
    res, value = alg.get_min()
    print(
        f"Coordonnées de l'individu minimal trouvé : {res[0], res[1]}"
    )
    print(
        f"Score de performance de l'individu minimal trouvé : {value}",
        Schwefel().eval(res),
    )"""

    """alg = AlgoGenetique(
       SixHumpCamelSix(),
       [[-5, 5], [-5, 5]],
       200,
       500,
       CodageBinaire([52, 10]),
       RoueDeLaFortune(),
       CroisementSimple(),
       MutationParPermutation(0.7),
    )
    res, value = alg.get_min()
    print(
        f"Coordonnées de l'individu minimal trouvé : {res[0], res[1]}"
    )
    print(f"Score de performance de l'individu minimal trouvé : {value}")"""

    """alg = AlgoGenetique(
        F2(),
        [[-2.048, 2.048], [-2.048, 2.048]],
        200,
        1000,
        CodageBinaire([52, 10]),
        RoueDeLaFortune(),
        CroisementSimple(),
        MutationParPermutation(0.7),
    )
    res, value = alg.get_min()
    print(
        f"Coordonnées de l'individu minimal trouvé : {res[0], res[1]}"
    )
    print(f"Score de performance de l'individu minimal trouvé : {value}")"""

    """alg = AlgoGenetique(
        F6(),
        [[-100, 100], [-100, 100]],
        100,
        100,
        CodageHexadecimal([52, 10]),
        RoueDeLaFortune(),
        CroisementSimple(),
        MutationParPermutation(0.7),
    )
    res, value = alg.get_min()
    print(
        f"Coordonnées de l'individu minimal trouvé : {res[0], res[1]}"
    )
    print(f"Score de performance de l'individu minimal trouvé : {value}")"""

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
        50,
        100,
        CodageBinaire([52, 10]),
        RoueDeLaFortune(),
        CroisementSimple(),
        MutationParPermutation(0.7),
    )
    res, value = alg.get_min()
    print(
        f"Coordonnées de l'individu minimal trouvé : {res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7], res[8], res[9]}"
    )
    print(f"Score de performance de l'individu minimal trouvé : {value}")"""

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
        50,
        200,
        CodageBinaire([52, 10]),
        Tournoi(0.8),
        CroisementSimple(),
        MutationParFlipping(0.7),
    )
    res, value = alg.get_min()
    print(
        f"Coordonnées de l'individu minimal trouvé : {res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7], res[8], res[9]}"
    )
    print(f"Score de performance de l'individu minimal trouvé : {value}")"""

    """alg = AlgoGenetique(
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
        500,
        CodageBinaire([52, 10]),
        RoueDeLaFortune(),
        CroisementSimple(),
        MutationParPermutation(0.6),
    )
    res, value = alg.get_min()
    print(
        f"Coordonnées de l'individu minimal trouvé : {res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7], res[8], res[9]}"
    )
    print(
        f"Score de performance de l'individu minimal trouvé : {value}", F9().eval(res)
    )
    """
    pass
