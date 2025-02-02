from Fenetre import Fenetre
from CodageBinaire import CodageBinaire
import random


# liste de fenetres
class Coordonnee:
    def __init__(self, fenetre, type_codage, valeur=None):
        if type(fenetre) != str:
            self.nom = fenetre  # nom de la variable
        else:
            self.nom = fenetre.nom
        if valeur is not None:
            self.valeur = valeur  # sa valeur
        else:
            self.valeur = random.uniform(fenetre.min, fenetre.max)
        self.type_codage = type_codage  # savoir dans quelle base ie quel objet on a
        self.code_base_x = (
            self.set_code_base_x()
        )  # avoir la conversion des coordonnées dans la base selectionnée

    def set_code_base_x(self):
        self.type_codage.code(self.valeur)

    def get_codage_coordonnee(self):
        return self.type_codage.code(self.valeur)

    def get_valeur_coordonnee(self):
        return self.valeur

    def set_valeur_coordonnee(self, fenetre, valeur=None):
        # Si aucune valeur n'est fournie, générer une valeur aléatoire entre xmin et xmax
        if valeur is None:
            self.valeur = random.uniform(fenetre.min, fenetre.max)
        else:
            self.valeur = valeur
