import random


class Mutation:
    def __init__(self, taux_mutation):
        """
        Initialise la classe Mutation.

        :param taux_mutation: Probabilité qu'un individu subisse une mutation.
        """
        self.taux_mutation = taux_mutation

    def effectuer_mutation(self, population):
        """
        Applique des mutations à une population d'individus.

        :param population: Une instance de la classe Population.
        :return: Une nouvelle instance de Population avec des mutations appliquées.
        """
        raise NotImplementedError(
            "Cette méthode doit être implémentée par les sous-classes."
        )
