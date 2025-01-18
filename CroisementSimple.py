import random
import itertools
from Croisement import Croisement
from Individu import Individu
from Coordonnee import Coordonnee


class CroisementSimple(Croisement):
    def __init__(self):
        super().__init__()

    def perform_crossover(self, ind1, ind2):
        """
        Effectue un croisement à un point pour chaque coordonnée des individus,
        avec une vérification des bornes imposées par les fenêtres.
        """
        enfants_par_variable = []

        for coord1, coord2 in zip(ind1.coordonnees, ind2.coordonnees):
            enfants_valides = []

            while len(enfants_valides) < 2:
                code1 = coord1.get_codage_coordonnee()
                code2 = coord2.get_codage_coordonnee()

                # Croisement à un point
                point_de_coupe = random.randint(1, len(code1) - 1)
                enfant1_code = code1[:point_de_coupe] + code2[point_de_coupe:]
                enfant2_code = code2[:point_de_coupe] + code1[point_de_coupe:]

                enfant1_valeur = coord1.type_codage.decode(enfant1_code)
                enfant2_valeur = coord2.type_codage.decode(enfant2_code)

                if coord1.nom.min <= enfant1_valeur <= coord1.nom.max:
                    enfants_valides.append(
                        Coordonnee(coord1.nom, coord1.type_codage, enfant1_valeur)
                    )
                if (
                    len(enfants_valides) < 2
                    and coord1.nom.min <= enfant2_valeur <= coord1.nom.max
                ):
                    enfants_valides.append(
                        Coordonnee(coord1.nom, coord1.type_codage, enfant2_valeur)
                    )

            enfants_par_variable.append(enfants_valides)

        enfants_complets = []
        for combinaison in itertools.product(*enfants_par_variable):
            enfants_complets.append(Individu(list(combinaison)))

        return enfants_complets


# Exemple d'utilisation
if __name__ == "__main__":
    from Fenetre import Fenetre
    from CodageBinaire import CodageBinaire

    # Création des fenêtres et du codage binaire
    fenetre_x = Fenetre("x", 0, 10)
    fenetre_y = Fenetre("y", 5, 15)
    fenetre_z = Fenetre("z", -5, 5)  # Ajout d'une troisième fenêtre
    codage = CodageBinaire([23, 8])

    # Création des individus avec leurs coordonnées
    ind1 = Individu(
        [
            Coordonnee(fenetre_x, codage, valeur=2.5),
            Coordonnee(fenetre_y, codage, valeur=7.3),
            Coordonnee(fenetre_z, codage, valeur=0.0),
        ]
    )
    ind2 = Individu(
        [
            Coordonnee(fenetre_x, codage, valeur=4.8),
            Coordonnee(fenetre_y, codage, valeur=10.2),
            Coordonnee(fenetre_z, codage, valeur=-3.4),
        ]
    )

    # Croisement simple
    croisement_simple = CroisementSimple()
    enfants_simple = croisement_simple.perform_crossover(ind1, ind2)

    # Afficher les enfants générés
    print("Enfants générés après croisement :")
    for enfant, i in zip(enfants_simple, range(len(enfants_simple))):
        print(f"Enfant {i}:")
        for coord in enfant.coordonnees:
            print(f"  {coord.nom.nom}: {coord.valeur}")
