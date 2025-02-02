from Codage import Codage
import math


class CodageHexadecimal(Codage):
    def __init__(self, precisions):
        self.precision_mantisse = precisions[0]
        self.precision_exposant = precisions[1]

    def code(self, coordonnee):
        sign = 0 if coordonnee >= 0 else 1
        coordonnee = abs(coordonnee)

        mantisse, exposant = math.frexp(coordonnee)
        exposant -= 1

        # Calcul des bits d'exposant et de mantisse
        exposant_bits = exposant + 2 ** (self.precision_exposant - 1) - 1
        mantisse_bits = int((mantisse - 0.5) * (2 ** (self.precision_mantisse + 1)))

        # Conversion en hexadécimal
        exposant_hex = f"{exposant_bits:0{self.precision_exposant // 4}X}"
        mantisse_hex = f"{mantisse_bits:0{self.precision_mantisse // 4}X}"

        # Chaîne finale en hexadécimal
        hex_str = f"{sign}{exposant_hex}{mantisse_hex}"
        return hex_str

    def decode(self, coordonnee):
        # Récupérer les parties sign, exposant, et mantisse
        sign = int(coordonnee[0], 16)
        exposant_hex = coordonnee[1 : 1 + (self.precision_exposant // 4)]
        mantisse_hex = coordonnee[1 + (self.precision_exposant // 4) :]

        # Conversion en valeurs décimales
        exposant = int(exposant_hex, 16) - 2 ** (self.precision_exposant - 1) + 1
        mantisse = 1 + int(mantisse_hex, 16) / (2**self.precision_mantisse)

        # Calcul de la valeur finale
        value = mantisse * (2**exposant)
        if sign == 1:
            value = -value
        return value


if __name__ == "__main__":
    nombre = 0
    codage = CodageHexadecimal([23, 8])
    binary_rep = codage.code(nombre)
    decoded_value = codage.decode(binary_rep)
    print(binary_rep, decoded_value)
