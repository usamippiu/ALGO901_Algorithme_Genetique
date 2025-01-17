from Selection import Selection

import numpy as np


class Tournoi(Selection):
    def __init__(self, p):
        self.p = p

    def tournoi(self, population):
        sorted(
            [individu for individu in population.individus],
            key=lambda x: x.score_performance,
        )
        pass

    def selection_parents(self, population):

        parent1 = self.roue_de_la_fortune(population)[0]
        parent2 = self.roue_de_la_fortune(population)[0]
        while parent1 == parent2:
            parent2 = self.roue_de_la_fortune(population)[0]

        return parent1, parent2


if __name__ == "__main__":
