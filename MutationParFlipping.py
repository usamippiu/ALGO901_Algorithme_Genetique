import random
from Mutation import Mutation


class MutationParFlipping(Mutation):
    def __init__(self, taux_mutation):
        """
        Initialise la classe MutationParFlipping.

        :param taux_mutation: Probabilité qu'un individu subisse une mutation.
        """
        super().__init__(taux_mutation)

    def effectuer_mutation(self, population):
        """
        Applique des mutations à une population d'individus.

        :param population: Une instance de la classe Population.
        :return: Une nouvelle instance de Population avec des mutations appliquées.
        """
        # Copie de la population initiale pour éviter de modifier l'originale
        nouvelle_population = population.copy()

        # Parcourir les individus et appliquer la mutation selon le taux
        for individu in nouvelle_population.individus:
            if (
                random.random() < self.taux_mutation
            ):  # On applique la mutation à cet individu
                for coord in individu.coordonnees:
                    mutation_valide = False
                    while not mutation_valide:
                        # On réucpère le codage binaire de la coordonnée
                        code = coord.get_codage_coordonnee()
                        # On choisit un bit aléatoire à inverser
                        bit_a_muter = random.randint(0, len(code) - 1)
                        code_mute = list(code)  # On transforme en liste pour modifier
                        code_mute[bit_a_muter] = (
                            "1" if code[bit_a_muter] == "0" else "0"
                        )
                        code_mute = "".join(code_mute)  # On reconstitue la chaîne

                        # On décode la valeur mutée
                        valeur_mutee = coord.type_codage.decode(code_mute)

                        # On vérifie si la valeur respecte les bornes de la fenêtre
                        if coord.nom.min <= valeur_mutee <= coord.nom.max:
                            mutation_valide = True
                            coord.valeur = valeur_mutee
        return nouvelle_population


if __name__ == "__main__":
    from Population import Population
    from Mutation import Mutation
    from Fenetre import Fenetre
    from CodageBinaire import CodageBinaire
    from Individu import Individu
    from Coordonnee import Coordonnee
    from F2 import F2

    # Définition des fenêtres et du codage
    fenetre_x = Fenetre("x", 0, 10)
    fenetre_y = Fenetre("y", -5, 5)
    codage = CodageBinaire([23, 8])

    # Génération de la population
    population = Population(1, F2())  # Population de 10 individus
    population.generer_population([fenetre_x, fenetre_y], codage)

    # Avant mutation
    print("Population avant mutation :")
    for individu in population.individus:
        print([coord.valeur for coord in individu.coordonnees])

    # Initialisation de la mutation
    taux_mutation = 1  # 1% de chance qu'un individu subisse une mutation
    mutation = MutationParFlipping(taux_mutation)
    population_mutée = mutation.effectuer_mutation(population)

    # Après mutation
    print("\nPopulation après mutation :")
    for individu in population_mutée.individus:
        print([coord.valeur for coord in individu.coordonnees])
