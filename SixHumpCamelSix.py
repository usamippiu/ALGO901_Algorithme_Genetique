from Performance import Performance


class SixHumpCamelSix(Performance):
    def eval(self, coordonees):
        x1, x2 = coordonees
        return (
            (4 - 2.1 * x1**2 + x1**4 / 3) * x1**2 + x1 * x2 + (-4 + 4 * x2**2 * x2**2)
        )


if __name__ == "__main__":
    func = SixHumpCamelSix("SixHumpCamelSix")
    print(func.eval([1, 1]))
