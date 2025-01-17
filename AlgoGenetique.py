from Fenetre import Fenetre
from Population import Population


class AlgoGenetique:
    def __init__(
        self,
        fonction,
        ranges,
        taille_population,
        nb_iter_max,
        codage,
    ):
        self.fonction = fonction
        self.nb_iter_max = nb_iter_max
        self.taille_population = taille_population
        self.fenetres = []
        for i in range(len(ranges)):
            self.fenetres.append(Fenetre(f"x{i}", ranges[i][0], ranges[i][1]))
        self.codage = codage
        self.population = Population(self.taille_population, self.fonction)

        self.population.generer_population(self.fenetres, self.codage)
        self.individu_min = self.population.lf_individu_minimal()

    def get_min(self):
        nb_iter = 0
        while nb_iter < self.nb_iter_max:
            pass


if __name__ == "__main__":
    alg = AlgoGenetique(10, 10, [[-10, 10], [-5, 5]])
    print(alg.fenetres[0].min)
