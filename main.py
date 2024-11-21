# IMPORTATION DES CLASSES ##############################################################################################
from Croisement import *
from Population import Population
from Performance import Performance
from Fenetre import Fenetre
from Codage import Codage
from CodageBinaire import CodageBinaire
from Selection import Selection
from RoueDeLaFortune import RoueDeLaFortune
from SelectionNouvelleGeneration import SelectionNouvelleGeneration

# Fonctions de performance :
from F2 import F2
from F6 import F6
from F7 import F7
from F8 import F8
from F9 import F9
from Schwefel import Schwefel
from SixHumpCamelSix import SixHumpCamelSix


# GENESE ###############################################################################################################

# Fonction a optimiser :
def f(x):
    return 0


# Nombre d'itérations max :
nb_iter_max = 10 ** 5

# Erreur d'approx de la solution:
epsilon = 10 ** (-12)

# Nombre maximum d'individus que l'on souhaite avoir dans notre population :
nombreMax = 100

# Nombre de coordonnées d'un individu
dimension = 2

# Fonction de mesure pour la performance de notre algorithme :
fonctionPerformance = F2("f2")  # TODO : Pourquoi donner un nom ?

# Fenêtres pour la génération de la population :
# TODO : Construire autant de fenêtres semble laborieux dans les cas où ce n'est pas les mêmes intervalles.
fenetres = []
for i in range(dimension):
    fenetres.append(Fenetre(0, 1, f"x{i}"))

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

# QUESTIONS #

# Comment le score pour chaque individu est déterminé ? Précision de l'évaluation ?
# Quand réduire la population ? À Evaluation ou mutation ?


# PSEUDO CODE #

# EVALUATION ###########################################################################################################
nb_iter = 0
while nb_iter < nb_iter_max:
    for individu in population.individus:
        continue
    #       Si le score d'un individu est supérieur à un score seuil (donnée par la précision souhaité):
    #       On renvoie l'individu comme solution
    #       On arrête l'algorithme.
    #

    # SELECTION ############################################################################################################
    population_copy = population.copy()
    couples = []
    RF = RoueDeLaFortune(population)
    while len(population_copy) > 1:
        [parent1, parent2] = RF.selection_parents()
        population_copy.supprimer_individus([parent1, parent2])
        couples.append([parent1, parent2])

    # CROISEMENT ###########################################################################################################
    enfants = []
    for couple in couples:
        croisement = CroisementSimple(couple)
        croisement.validate_individuals()
        [enfant1, enfant2], _, _ = croisement.perform_crossover()
        enfants += [enfant1, enfant2]

    # MUTATION #############################################################################################################
    nouv_gen = SelectionNouvelleGeneration(population, enfant, mutation=None)  # todo : mutation ???
    enfants_selct = nouv_gen.selection_nouvelle_generation()
    population.ajouter_individus(enfants_selct)
    # todo : supprimer le surplus de la population dont le score est le plus bas.
    nb_iter += 1  # Si le nombre max d'itérations est atteint, on renvoie l'individu avec le score le plus élevé.
