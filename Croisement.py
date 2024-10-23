import random


class Croisement:
    def __init__(self, selected_individuals):
        """
        Initialisation de la classe Croisement avec les individus sélectionnés.

        :param selected_individuals: Liste de chaînes binaires représentant les individus sélectionnés.
        """
        self.selected_individuals = selected_individuals

    def validate_individuals(self):
        """
        Valide que tous les individus ont la même longueur.
        """
        length = len(self.selected_individuals[0])
        for ind in self.selected_individuals:
            if len(ind) != length:
                raise ValueError("Tous les individus doivent avoir la même longueur.")

    def perform_crossover(self):
        """
        Méthode à implémenter dans les classes dérivées pour effectuer le croisement.
        """
        raise NotImplementedError(
            "Cette méthode doit être implémentée par les sous-classes."
        )


class CroisementSimple(Croisement):
    def __init__(self, selected_individuals):
        super().__init__(selected_individuals)

    def perform_crossover(self, points_de_coupe=1):
        """
        Effectue le croisement entre deux individus selon un point de découpe.

        :param points_de_coupe: Nombre de points de découpe à utiliser pour le croisement (doit être 1).
        :return: Liste des individus générés par le croisement.
        """
        # Valider les individus
        self.validate_individuals()

        # Récupérer les individus sélectionnés
        ind1, ind2 = self.selected_individuals

        # Longueur du chromosome
        length = len(ind1)

        if points_de_coupe != 1:
            raise ValueError(
                "Le nombre de points de découpe doit être 1 pour le croisement simple."
            )

        # Créer un point de découpe aléatoire
        point_de_coupe = random.randint(1, length - 1)

        # Effectuer le croisement
        enfant1 = ind1[:point_de_coupe] + ind2[point_de_coupe:]
        enfant2 = ind2[:point_de_coupe] + ind1[point_de_coupe:]

        return [enfant1, enfant2]


# Exemple d'utilisation
if __name__ == "__main__":
    individus = ["1010011", "1110010"]
    croisement = CroisementSimple(individus)
    enfants = croisement.perform_crossover(points_de_coupe=1)

    # Afficher les enfants générés
    for enfant in enfants:
        print(enfant)
