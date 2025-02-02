import random
from Mutation import Mutation


class MutationParPermutation(Mutation):
    def __init__(self, taux_mutation):
        """
        Initialise la classe MutationParPermutation.

        :param taux_mutation: Probabilité qu'un individu subisse une mutation.
        """
        super().__init__(taux_mutation)

    def effectuer_mutation(self, population):
        """
        Applique des mutations globales à une population d'individus.

        :param population: Une instance de la classe Population.
        :return: Une nouvelle instance de Population avec des mutations appliquées.
        """

        # Parcourir les individus et appliquer la mutation selon le taux
        for individu in population.individus:
            if (
                random.random() < self.taux_mutation
            ):  # On applique la mutation à cet individu
                for coord in individu.coordonnees:
                    mutation_valide = False
                    while not mutation_valide:
                        # Récupérer le codage binaire de la coordonnée
                        code = coord.get_codage_coordonnee()
                        code_list = list(code)

                        # On sélectionne deux positions distinctes
                        pos1, pos2 = random.sample(range(len(code_list)), 2)

                        # On échange les bits
                        code_list[pos1], code_list[pos2] = (
                            code_list[pos2],
                            code_list[pos1],
                        )
                        code_mute = "".join(code_list)

                        # On décode la valeur mutée
                        valeur_mutee = coord.type_codage.decode(code_mute)

                        # On vérifie si la valeur respecte les bornes de la fenêtre
                        if coord.nom.min <= valeur_mutee <= coord.nom.max:
                            mutation_valide = True
                            coord.valeur = valeur_mutee
                individu.set_score_performance(population)


if __name__ == "__main__":
    from Population import Population
    from Fenetre import Fenetre
    from CodageBinaire import CodageBinaire
    from CodageHexadecimal import CodageHexadecimal
    from Individu import Individu
    from Coordonnee import Coordonnee
    from F2 import F2

    # Définition des fenêtres et du codage
    fenetre_x = Fenetre("x", 0, 10)
    fenetre_y = Fenetre("y", -5, 5)
    codage = CodageHexadecimal([23, 8])

    # Génération de la population
    population = Population(1, F2())  # Population de 1 individu pour l'exemple
    population.generer_population([fenetre_x, fenetre_y], codage)

    # Avant mutation
    print("Population avant mutation :")
    for individu in population.individus:
        print([coord.valeur for coord in individu.coordonnees])

    # Initialisation de la mutation globale
    taux_mutation = (
        1  # 100% de chance qu'un individu subisse une mutation pour l'exemple
    )
    mutation_globale = MutationParPermutation(taux_mutation)
    population_mutée = mutation_globale.effectuer_mutation(population)

    # Après mutation
    print("\nPopulation après mutation globale :")
    for individu in population_mutée.individus:
        print([coord.valeur for coord in individu.coordonnees])
