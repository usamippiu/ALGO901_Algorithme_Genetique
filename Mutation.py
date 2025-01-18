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
                    # On obtient le codage binaire de la coordonnée
                    code = coord.get_codage_coordonnee()

                    # On choisit un bit aléatoire à inverser
                    bit_a_muter = random.randint(0, len(code) - 1)
                    code_muté = list(
                        code
                    )  # On transforme la chaîne en liste pour modification
                    code_muté[bit_a_muter] = "1" if code[bit_a_muter] == "0" else "0"
                    code_muté = "".join(code_muté)  # Reconstituer la chaîne mutée

                    # On décode la valeur mutée
                    valeur_mutée = coord.type_codage.decode(code_muté)

                    # On vérifie si la valeur mutée respecte les bornes de la fenêtre
                    if coord.nom.min <= valeur_mutée <= coord.nom.max:
                        mutation_valide = True
                        # On applique la mutation
                        coord.valeur = valeur_mutée
                        coord.type_codage.code = code_muté  # On met à jour le codage

        return individu


if __name__ == "__main__":
    from Fenetre import Fenetre
    from CodageBinaire import CodageBinaire
    from Individu import Individu
    from Coordonnee import Coordonnee
    from Mutation import Mutation

    # Définition des fenêtres et du codage
    fenetre_x = Fenetre("x", 0, 10)
    codage = CodageBinaire([23, 8])  # Longueur fixe de 5 bits

    # Création d'un individu
    individu = Individu(
        [
            Coordonnee(fenetre_x, codage, valeur=2.5),
        ]
    )

    # Initialisation de la mutation avec un taux faible
    taux_mutation = 0.001
    mutation = Mutation(taux_mutation)

    # Individu avant la mutation
    print("Individu avant mutation :")
    for coord in individu.coordonnees:
        print(
            f"{coord.nom.nom}: {coord.valeur} (code: {coord.get_codage_coordonnee()})"
        )

    # Mutation
    individu_muté = mutation.effectuer_mutation(individu)

    # Individu après la mutation
    print("\nIndividu après mutation :")
    for coord in individu_muté.coordonnees:
        print(
            f"{coord.nom.nom}: {coord.valeur} (code: {coord.get_codage_coordonnee()})"
        )
