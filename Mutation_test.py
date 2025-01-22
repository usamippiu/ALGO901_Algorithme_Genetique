import unittest
from MutationParFlipping import MutationParFlipping
from MutationParPermutation import MutationParPermutation
from Population import Population
from F2 import F2


class TestMutationMethods(unittest.TestCase):
    def test_type_retour(self):
        population = Population(1, F2())
        taux_mutation = 1
        mutation_flipping = MutationParFlipping(taux_mutation)
        self.assertEqual(
            type(mutation_flipping.effectuer_mutation(population)), Population
        )

        mutation_permutation = MutationParPermutation(taux_mutation)
        self.assertEqual(
            type(mutation_permutation.effectuer_mutation(population)), Population
        )

    def test_taille_population(self):
        population = Population(10, F2())
        taux_mutation = 1
        mutation_flipping = MutationParFlipping(taux_mutation)
        self.assertEqual(
            len(mutation_flipping.effectuer_mutation(population).individus),
            len(population.individus),
        )


if __name__ == "__main__":
    unittest.main()
