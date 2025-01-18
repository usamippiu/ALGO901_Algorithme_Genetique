import random
from Coordonnee import Coordonnee
from Individu import Individu


class Mutation:
    def __init__(self, taux_mutation):
        """
        Initialise la classe Mutation.

        :param taux_mutation: Probabilité qu'un individu soit muté (ex. 0.001).
        """
        self.taux_mutation = taux_mutation

    def effectuer_mutation(self, individu):
        """
        Effectue une mutation sur un individu avec le taux de mutation spécifié.
        Si une mutation est déclenchée, un bit aléatoire d'une coordonnée de l'individu
        est modifié. La mutation est répétée jusqu'à ce que l'individu muté respecte
        les bornes des fenêtres associées.

        :param individu: L'individu à muter (objet Individu).
        :return: L'individu potentiellement muté.
        """
        for coord in individu.coordonnees:
            if random.random() < self.taux_mutation:
                mutation_valide = False

                while not mutation_valide:
                    # Obtenir le codage binaire de la coordonnée
                    code = coord.get_codage_coordonnee()

                    # Choisir un bit aléatoire à inverser
                    bit_a_muter = random.randint(0, len(code) - 1)
                    code_muté = list(
                        code
                    )  # Transformer la chaîne en liste pour modification
                    code_muté[bit_a_muter] = "1" if code[bit_a_muter] == "0" else "0"
                    code_muté = "".join(code_muté)  # Reconstituer la chaîne mutée

                    # Décoder la valeur mutée
                    valeur_mutée = coord.type_codage.decode(code_muté)

                    # Vérifier si la valeur mutée respecte les bornes de la fenêtre
                    if coord.nom.min <= valeur_mutée <= coord.nom.max:
                        mutation_valide = True
                        # Appliquer la mutation
                        coord.valeur = valeur_mutée
                        coord.type_codage.code = code_muté  # Mettre à jour le codage

        return individu
