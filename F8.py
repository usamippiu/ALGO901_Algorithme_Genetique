from Performance import Performance
import numpy as np


class F8(Performance):
    def eval(self, coordonees):
        return (
            1
            + sum(x**2 / 4000 for x in coordonees)
            - np.prod([np.cos(x / np.sqrt(i + 1)) for i, x in enumerate(coordonees)])
        )


if __name__ == "__main__":
    func = F8("F8")
    print(func.eval([0] * 10))
