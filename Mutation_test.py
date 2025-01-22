import unittest
from MutationParFlipping import MutationParFlipping
from Population import Population
from F2 import F2


class TestMutationMethods(unittest.TestCase):
    def test_indidual_length(self):
        population = Population(1, F2())
        taux_mutation = 1
        mutation = MutationParFlipping(taux_mutation)
        self.assertEqual(type(mutation.effectuer_mutation(population)), Population)


if __name__ == "__main__":
    unittest.main()
