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

# Fonctions de selection :
from RoueDeLaFortune import RoueDeLaFortune
from Selection import Selection

# Fonction de crossover
from Croisement import Croisement, CroisementSimple
# from CroisementSimple import CroisementSimple
# from Croisement import Croisement


# Import PY libraries
import matplotlib.pyplot as plt

tirageMax = 1
# Stockons les individus pour voir si on arrive ou non à améliorer le score 
individus_min = [ ]
for i in range(tirageMax):
    # GENESE ###############################################################################################################

    # Nombre maximum d'individus que l'on souhaite avoir dans notre population :
    nombreMax = 100
    # Nombre de coordonnées d'un individu
    dimension = 2
    # Fonction de mesure pour la performance de notre algorithme :
    fonctionPerformance = F2("f2")

    # Fenêtres pour la génération de la population :
    fenetres  = []
    for i in range(dimension):
        fenetres.append(Fenetre(0,1,f"x{i}"))

    # Type de codage pour les coordonnées de chaque futur individus :
    # TODO : Mettre precision_mantisse et precision_exposant en paramètres séparés du constructeur comme cela on voit qui correspond à quoi.
    precision_mantisse = 52
    precision_exposant = 11
    typeCodage = CodageBinaire((precision_mantisse, precision_exposant))

    # Générer une population, on a des individus aléatoires avec des coordonnées dans les fenêtres et leurs score de performance en fonction d'une fonction choisie :
    population = Population(nombreMax, fonctionPerformance)
    population.generer_population(fenetres, typeCodage)
    # On cherche l'individu qui a le score de performance minimale et on le stock
    individu_min = population.lf_individu_minimal()
    individus_min.append(individu_min)
    
    # Choix de la selection
    selection = RoueDeLaFortune(population)
    parents1, parents2 = selection.selection_parents()
    # Crossover

scores = [individu.scorePerformance for individu in individus_min]

# Affichage pour la convergence de l'algo
''' indices = list(range(tirageMax))

plt.plot(indices, scores, marker='o', linestyle='-', color='b', label='Valeurs')
plt.title("Score minimal en fonction des tirages")
plt.xlabel("Tirage")
plt.xlim(0,tirageMax)
plt.ylabel("Score minimal")
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show() '''

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



