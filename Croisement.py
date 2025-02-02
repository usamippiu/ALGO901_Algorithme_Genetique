import random
import itertools
from Individu import Individu
from Fenetre import Fenetre
from Coordonnee import Coordonnee


class Croisement:
    def __init__(self):
        """
        Classe de base pour le croisement.
        """
        pass

    def perform_crossover(self, ind1, ind2):
        """
        Méthode à implémenter dans les classes dérivées pour effectuer le croisement.

        :param ind1: Premier individu (objet Individu).
        :param ind2: Deuxième individu (objet Individu).
        """
        raise NotImplementedError(
            "Cette méthode doit être implémentée par les sous-classes."
        )
