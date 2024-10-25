import numpy as np
from Performance import Performance


class Schwefel(Performance):
    def eval(self, coordonees):
        return sum(-x * np.sin(np.sqrt(abs(x))) for x in coordonees)
