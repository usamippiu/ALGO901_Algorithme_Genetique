from Fenetre import Fenetre
from Population import Population
from RoueDeLaFortune import RoueDeLaFortune
from Tournoi import Tournoi
from CodageBinaire import CodageBinaire
from CodageHexadecimal import CodageHexadecimal
from Carre import F
from Croisement import CroisementSimple


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
                enfant1, enfant2 = self.croisement.perform_crossover(
                    couple[0], couple[1]
                )
                enfants += [enfant1, enfant2]

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
    alg = AlgoGenetique(
        F(),
        [[-10, 10]],
        50,
        50,
        CodageHexadecimal([52, 11]),
        Tournoi(0.9),
        CroisementSimple(),
    )
    print(alg.get_min()[1])
