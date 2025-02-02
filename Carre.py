from Performance import Performance
import numpy as np


class F(Performance):
    def eval(self, coordonees):
        x1 = coordonees[0]
        return (x1 + 1) ** 2
