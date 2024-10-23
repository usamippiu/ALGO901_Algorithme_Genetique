import math


class Codage:
    def code(self, individu):
        pass

    def decode(self, individu):
        pass


class CodageBinaire:
    def code(self, individu):
        sign = 0 if individu >= 0 else 1
        individu = abs(individu)

        mantisse, exposant = math.frexp(individu)
        exposant -= 1

        exposant_bits = exposant + 1023

        mantisse_bits = int((mantisse - 0.5) * (2**53))

        exposant_bin = f"{exposant_bits:011b}"
        mantisse_bin = f"{mantisse_bits:052b}"

        binary_str = f"{sign}{exposant_bin}{mantisse_bin}"
        return binary_str

    def decode(self, individu):
        sign = int(individu[0], 2)
        exposant_bin = individu[1:12]
        mantisse_bin = individu[12:]

        exposant = int(exposant_bin, 2) - 1023
        mantisse = 1 + int(mantisse_bin, 2) / (2**52)

        value = mantisse * (2**exposant)
        if sign == 1:
            value = -value
        return value
