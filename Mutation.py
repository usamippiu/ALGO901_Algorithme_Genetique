import random


class Mutation:
    def __init__(self, taux_mutation):
        """
        Initialise la classe Mutation.

        :param taux_mutation: Probabilité qu'un individu subisse une mutation (ex. 0.01 pour 1%).
        """
        self.taux_mutation = taux_mutation

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
            ):  # Appliquer la mutation à cet individu
                for coord in individu.coordonnees:
                    mutation_valide = False
                    while not mutation_valide:
                        # Obtenir le codage binaire de la coordonnée
                        code = coord.get_codage_coordonnee()

                        # Choisir un bit aléatoire à inverser
                        bit_a_muter = random.randint(0, len(code) - 1)
                        code_muté = list(code)  # Transformer en liste pour modifier
                        code_muté[bit_a_muter] = (
                            "1" if code[bit_a_muter] == "0" else "0"
                        )
                        code_muté = "".join(code_muté)  # Reconstituer la chaîne

                        # Décoder la valeur mutée
                        valeur_mutée = coord.type_codage.decode(code_muté)

                        # Vérifier si la valeur respecte les bornes de la fenêtre
                        if coord.nom.min <= valeur_mutée <= coord.nom.max:
                            mutation_valide = True
                            coord.valeur = valeur_mutée
                            coord.type_codage.code = (
                                code_muté  # Mettre à jour le codage
                            )
        return nouvelle_population


if __name__ == "__main__":
    from Population import Population
    from Mutation import Mutation
    from Fenetre import Fenetre
    from CodageBinaire import CodageBinaire
    from Individu import Individu
    from Coordonnee import Coordonnee

    # Définition des fenêtres et du codage
    fenetre_x = Fenetre("x", 0, 10)
    fenetre_y = Fenetre("y", -5, 5)
    codage = CodageBinaire([23, 8])

    # Génération de la population
    population = Population(10, None)  # Population de 10 individus
    population.generer_population([fenetre_x, fenetre_y], codage)

    # Avant mutation
    print("Population avant mutation :")
    for individu in population.individus:
        print([coord.valeur for coord in individu.coordonnees])

    # Initialisation de la mutation
    taux_mutation = 0.01  # 1% de chance qu'un individu subisse une mutation
    mutation = Mutation(taux_mutation)
    population_mutée = mutation.effectuer_mutation(population)

    # Après mutation
    print("\nPopulation après mutation :")
    for individu in population_mutée.individus:
        print([coord.valeur for coord in individu.coordonnees])
