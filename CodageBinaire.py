import math


class Codage:
    def code(self, coordonnee):
        pass

    def decode(self, coordonnee):
        pass


class CodageBinaire:
    def code(self, coordonnee):
        sign = 0 if coordonnee >= 0 else 1
        coordonnee = abs(coordonnee)

        mantisse, exposant = math.frexp(coordonnee)
        exposant -= 1

        exposant_bits = exposant + 1023

        mantisse_bits = int((mantisse - 0.5) * (2**53))

        exposant_bin = f"{exposant_bits:011b}"
        mantisse_bin = f"{mantisse_bits:052b}"

        binary_str = f"{sign}{exposant_bin}{mantisse_bin}"
        return binary_str

    def decode(self, coordonnee):
        sign = int(coordonnee[0], 2)
        exposant_bin = coordonnee[1:12]
        mantisse_bin = coordonnee[12:]

        exposant = int(exposant_bin, 2) - 1023
        mantisse = 1 + int(mantisse_bin, 2) / (2**52)

        value = mantisse * (2**exposant)
        if sign == 1:
            value = -value
        return value


if __name__ == "__main__":
    nombre = 1.001
    codage = CodageBinaire()
    binary_rep = codage.code(nombre)
    decoded_value = codage.decode(binary_rep)
    print(binary_rep, decoded_value)
