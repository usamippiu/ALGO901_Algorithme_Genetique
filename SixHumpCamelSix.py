from Performance import Performance


class SixHumpCamelSix(Performance):

    def __init__(self):
        self.nom = "SixHumpCamelSix"

    def eval(self, coordonees):
        x1, x2 = coordonees
        return (
            (4 - 2.1 * x1**2 + x1**4 / 3) * x1**2 + x1 * x2 + (-4 + 4 * x2**2) * x2**2
        )


if __name__ == "__main__":
    func = SixHumpCamelSix()
    print(func.eval([0.0898, -0.7126]))
