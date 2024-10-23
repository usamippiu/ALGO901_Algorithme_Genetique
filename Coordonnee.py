# Importer la classe fenêtre pour initialiser les coordonnées
# Importer la classe codage
from Fenetre import Fenetre
from CodageBinaire import Codage, CodageBinaire

class coordonnees:
    def __init__(self, valeur, fenetre, typeCodage):
        self.nom = fenetre.nom  # liste de string par exemple dans R^3 on aurait [x,y,z]
        self.valeur = valeur    # liste de valeurs correspondantes, par exemple dans R^3 on aurait (2,4,5)
                                # cette liste contient des valeurs entre le min et le max de la taille de la fenêtre
        self.typeCodage = typeCodage # savoir dans quelle base
        self.codeBaseX = self.setCodeBaseX() # avoir la conversion des coordonnées dans la base selectionnée
        
    def setCodeBaseX(self):
       return self.codage.code(self.valeurs)

    def getCodageCoordonnees(self):
        return self.codeBaseX()
    
    def getCoordonnees(self):
        return self.valeur
