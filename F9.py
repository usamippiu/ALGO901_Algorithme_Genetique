from Performance import Performance
import numpy as np


class F9(Performance):
    def eval(self, coordonees):
        return 10 + sum(-x * np.sin(np.sqrt(np.abs(x))) for x in coordonees)


if __name__ == "__main__":
    func = F9("F9")
    print(func.eval(1, [420.9687] * 10))
