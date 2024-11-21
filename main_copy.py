# IMPORTATION DES CLASSES ##############################################################################################
from Population import Population
from Performance import Performance
from Fenetre import Fenetre
from Codage import Codage
from CodageBinaire import CodageBinaire
from Selection import Selection

# Fonctions de performance :
from F2 import F2
from F6 import F6
from F7 import F7
from F8 import F8
from F9 import F9
from Schwefel import Schwefel
from SixHumpCamelSix import SixHumpCamelSix

# GENESE ###############################################################################################################

# Nombre maximum d'individus que l'on souhaite avoir dans notre population :
nombreMax = 100
# Nombre de coordonnées d'un individu
dimension = 2
# Fonction de mesure pour la performance de notre algorithme :
fonctionPerformance = F2("f2") # TODO : Pourquoi donner un nom ?

# Fenêtres pour la génération de la population :
# TODO : Construire autant de fenêtres semble laborieux dans les cas où ce n'est pas les mêmes intervalles.
fenetres  = []
for i in range(dimension):
    fenetres.append(Fenetre(0,1,f"x{i}"))

# Type de codage pour les coordonnées de chaque futur individus :
# TODO : Mettre precision_mantisse et precision_exposant en paramètres séparés du constructeur comme cela on voit qui correspond à quoi.
precision_mantisse = 52
precision_exposant = 11
typeCodage = CodageBinaire((precision_mantisse, precision_exposant))

# Création de la population :
population = Population(nombreMax, fonctionPerformance)

# Générer une population :
population.generer_population(fenetres, typeCodage)
population.afficher_population()

# EVALUATION ###########################################################################################################



# Précision de l'évaluation ?
# Nombre d'itérations max ? -> nombre d'individus maximum par population ?
# Comment est determine les dimensions des individus ?


# PSEUDO CODE
# TANT QUE nb_iter max > 0:
#   POUR chaque individu dans la population :
#       Si le score d'un individu est supérieur à un score seuil (donnée par la précision souhaité):
#           On renvoie l'individu comme solution
#           On arrête l'algorithme

# SELECTION ############################################################################################################

#   population_copie <- population.copy()
#   couples <- []
#   RF <- RoudeDeLaFortune(population)
#   TANT QUE taille de la copie > 1:
#       [parent1, parent2] <- RF.selection_parents()
#       population_copie.supprimer_individus([parent1, parent2])
#       couples.append([parent1, parent2])

# CROISEMENT ###########################################################################################################



