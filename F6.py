from Performance import Performance
import numpy as np


class F6(Performance):
    def eval(self, coordonees):
        x, y = coordonees
        numerateur = np.sin(np.sqrt(x**2 + y**2)) ** 2 - 0.5
        denominateur = (1 + 0.001 * (x**2 + y**2)) ** 2
        return 0.5 + numerateur / denominateur


if __name__ == "__main__":
    func = F6("F6")
    print(func.eval([0, 0]))
