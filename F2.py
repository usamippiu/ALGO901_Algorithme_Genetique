from Performance import Performance


class F2(Performance):
    def eval(self, coordonees):
        x1, x2 = coordonees
        return 100 * (x1**2 - x2) ** 2 + (1 - x1) ** 2


if __name__ == "__main__":
    func = F2("F2")
    print(func.eval([1, 1]))
