import numpy as np


class Performance:
    def __init__(self, nom):
        self.nom = nom

    def eval(self, coordonees):
        pass


class Schwefel:
    def eval(self, coordonees):
        if len(coordonees) > 2:
            raise ValueError("La longueur des coordonnées ne doit pas dépasser 2.")

        x = coordonees[0]
        y = coordonees[1]
        return (-x * np.sin(np.sqrt(abs(x)))) + (-y * np.sin(np.sqrt(abs(y))))
