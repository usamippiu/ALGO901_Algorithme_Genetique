from Performance import Performance
import numpy as np


class F7(Performance):

    def __init__(self):
        self.nom = "F7"

    def eval(self, coordonees):
        return 200 + sum(x**2 - 10 * np.cos(2 * np.pi * x) for x in coordonees)


if __name__ == "__main__":
    func = F7()
    print(func.eval([0] * 10))
