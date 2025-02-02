import math
from Codage import Codage


class CodageBinaire(Codage):
    def __init__(self, precisions):
        self.precision_mantisse = precisions[0]
        self.precision_exposant = precisions[1]

    def code(self, coordonnee):
        sign = 0 if coordonnee >= 0 else 1
        coordonnee = abs(coordonnee)

        mantisse, exposant = math.frexp(coordonnee)
        exposant -= 1

        exposant_bits = exposant + 2 ** (self.precision_exposant - 1) - 1

        mantisse_bits = int((mantisse - 0.5) * (2 ** (self.precision_mantisse + 1)))

        exposant_bin = f"{exposant_bits:0{self.precision_exposant}b}"
        mantisse_bin = f"{mantisse_bits:0{self.precision_mantisse}b}"

        binary_str = f"{sign}{exposant_bin}{mantisse_bin}"
        return binary_str

    def decode(self, coordonnee):
        sign = int(coordonnee[0], 2)
        exposant_bin = coordonnee[1 : 1 + self.precision_exposant]
        mantisse_bin = coordonnee[1 + self.precision_exposant :]

        exposant = int(exposant_bin, 2) - 2 ** (self.precision_exposant - 1) + 1
        mantisse = 1 + int(mantisse_bin, 2) / (2**self.precision_mantisse)

        value = mantisse * (2**exposant)
        if sign == 1:
            value = -value
        return value


if __name__ == "__main__":
    nombre = 1.001
    codage = CodageBinaire([23, 8])
    binary_rep = codage.code(nombre)
    decoded_value = codage.decode(binary_rep)
    print(binary_rep, decoded_value)
