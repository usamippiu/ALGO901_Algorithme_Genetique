# Importer la classe fenêtre pour initialiser les coordonnées
# Importer la classe codage
from Fenetre import Fenetre
from CodageBinaire import CodageBinaire
import random

# liste de fenetres
class Coordonnee:
    def __init__(self, fenetre, typeCodage, valeur=None):
        self.nom = fenetre.nom  # nom de la variable
        if valeur is not None:
            self.valeur = valeur    # sa valeur
        self.typeCodage = typeCodage # savoir dans quelle base ie quel objet on a
        self.codeBaseX = self.set_code_base_X() # avoir la conversion des coordonnées dans la base selectionnée
        
    def set_code_base_X(self):
       return self.typeCodage.code(self.valeur)

    def get_codage_coordonnee(self):
        return self.codeBaseX()
    
    def get_valeur_coordonnee(self):
        return self.valeur
    
    def set_valeur_coordonnee(self, fenetre, valeur=None):
        # Si aucune valeur n'est fournie, générer une valeur aléatoire entre xmin et xmax
        if valeur is None:
            valeur = random.uniform(fenetre.min, fenetre.max)
        return valeur
            
