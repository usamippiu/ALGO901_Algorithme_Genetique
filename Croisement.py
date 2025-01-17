import random
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


class CroisementSimple(Croisement):
    def __init__(self):
        super().__init__()

    def perform_crossover(self, ind1, ind2):
        """
        Effectue un croisement à un point sur chaque coordonnée des individus.

        :param ind1: Premier individu (objet Individu).
        :param ind2: Deuxième individu (objet Individu).
        :return: Liste des individus enfants générés par le croisement.
        """
        enfants = [Individu([]), Individu([])]  # Créer deux enfants vides

        for coord1, coord2 in zip(ind1.coordonnees, ind2.coordonnees):
            # On récupére les codages binaires des coordonnées
            code1 = coord1.get_codage_coordonnee()
            code2 = coord2.get_codage_coordonnee()

            # On effectue le croisement à un point de découpe
            point_de_coupe = random.randint(1, len(code1) - 1)
            enfant1_code = code1[:point_de_coupe] + code2[point_de_coupe:]
            enfant2_code = code2[:point_de_coupe] + code1[point_de_coupe:]

            # On décode les nouveaux codes en valeurs
            enfant1_valeur = coord1.typeCodage.decode(enfant1_code)
            enfant2_valeur = coord2.typeCodage.decode(enfant2_code)

            # On attribue les nouvelles coordonnées aux enfants
            enfants[0].coordonnees.append(
                Coordonnee(coord1.nom, coord1.typeCodage, enfant1_valeur)
            )
            enfants[1].coordonnees.append(
                Coordonnee(coord2.nom, coord2.typeCodage, enfant2_valeur)
            )

        return enfants


class CroisementDouble(Croisement):
    def __init__(self):
        super().__init__()

    def perform_crossover(self, ind1, ind2):
        """
        Effectue un croisement à deux points sur chaque coordonnée des individus.

        :param ind1: Premier individu (objet Individu).
        :param ind2: Deuxième individu (objet Individu).
        :return: Liste des individus enfants générés par le croisement.
        """
        enfants = [Individu([]), Individu([])]  # Créer deux enfants vides

        for coord1, coord2 in zip(ind1.coordonnees, ind2.coordonnees):
            # On récupére les codages binaires des coordonnées
            code1 = coord1.get_codage_coordonnee()
            code2 = coord2.get_codage_coordonnee()

            # On effectue le croisement à deux points de découpe
            point1, point2 = sorted(random.sample(range(1, len(code1)), 2))
            enfant1_code = code1[:point1] + code2[point1:point2] + code1[point2:]
            enfant2_code = code2[:point1] + code1[point1:point2] + code2[point2:]

            # On décode les nouveaux codes en valeurs
            enfant1_valeur = coord1.typeCodage.decode(enfant1_code)
            enfant2_valeur = coord2.typeCodage.decode(enfant2_code)

            # On attribue les nouvelles coordonnées aux enfants
            enfants[0].coordonnees.append(
                Coordonnee(coord1.nom, coord1.typeCodage, enfant1_valeur)
            )
            enfants[1].coordonnees.append(
                Coordonnee(coord2.nom, coord2.typeCodage, enfant2_valeur)
            )

        return enfants


# Exemple d'utilisation
if __name__ == "__main__":
    # Création de la fenêtre et du codage binaire
    from Fenetre import Fenetre
    from CodageBinaire import CodageBinaire

    fenetre = Fenetre("x", 0, 10)  # Exemple de fenêtre
    codage = CodageBinaire([23, 8])  # Exemple de codage

    # Création des individus avec leurs coordonnées
    ind1 = Individu(
        [
            Coordonnee(fenetre, codage, valeur=2.5),
            Coordonnee(fenetre, codage, valeur=7.3),
        ]
    )
    ind2 = Individu(
        [
            Coordonnee(fenetre, codage, valeur=4.8),
            Coordonnee(fenetre, codage, valeur=1.2),
        ]
    )

    # Croisement simple
    croisement_simple = CroisementSimple()
    enfants_simple = croisement_simple.perform_crossover(ind1, ind2)
    print("Enfants après croisement simple :")
    for enfant in enfants_simple:
        for coord in enfant.coordonnees:
            print(f"Nom: {coord.nom}, Valeur: {coord.valeur}")

    # Croisement double
    croisement_double = CroisementDouble()
    enfants_double = croisement_double.perform_crossover(ind1, ind2)
    print("\nEnfants après croisement double :")
    for enfant in enfants_double:
        for coord in enfant.coordonnees:
            print(f"Nom: {coord.nom}, Valeur: {coord.valeur}")
