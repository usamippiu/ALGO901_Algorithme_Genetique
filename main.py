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

# Mode bencmark de l'algorithme :
benchmark = False

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
fonctionPerformance = F2("f2")

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
individu_min = population.lf_individu_minimal()


# QUESTIONS #

# Comment le score pour chaque individu est déterminé ? Précision de l'évaluation ?
# Quand réduire la population ? À Evaluation ou mutation ?


# PSEUDO CODE #

# EVALUATION ###########################################################################################################

# Initialisation du nombre d'itérations :
nb_iter = 0

# Tant que le nombre d'itérations max n'est pas atteint :
while nb_iter < nb_iter_max:
    # On sélectionne le meilleur individus. Dépend de si nous sommes en mode benchmark ou non.
    # todo : Créer un attribut meilleur_individu, soit dans la classe Population, soit dans une future classe AlgoGenetique.
    if benchmark:
        continue
        # On prend l'individu avec le meilleur score de performance sur la fonction de benchmark.
        # todo : écrire méthode dans Population qui renvoie l'individu avec le meilleur score de performance.
    else:
        continue
        # On sélectionne l'individu qui minimise le mieux la fonction à optimiser
        # todo : méthode dans population qui renvoie l'individu qui minimise le mieux notre fonction d'optimisation.

# SELECTION ############################################################################################################
    # On sélectionne les parents sur une copie de la population.
    # On arrête une fois qu'aucuns couple ne peut être formé :

    # Population de sélection des couples :
    population_copy = population.copy()

    # Liste des couples :
    couples = []

    # Initialisation de la méthode de sélection : todo : Préciser la méthode pendant la génèse.
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
        # Remplacement aléatoire enfants/parents
        #       -> On supprime les 2 individus non-sélectionner parmis le quatuor parent/enfant.
        #       -> La sélection se fait avec la classe SélectionNouvelleGénération
        # On remplace dans la population
        # todo : la mutation a lieu pendant le croisement avec les parents
        # todo : sélection de la nouvelle génération devrait aléatoirement choisir deux individus parmis 4 : parent1, parent2, enfant1, enfant2
        enfants += [enfant1, enfant2]

    # MUTATION #############################################################################################################
    nouv_gen = SelectionNouvelleGeneration(population, enfants, mutation=None)  # todo : mutation ???
    enfants_selct = nouv_gen.selection_nouvelle_generation()
    population.ajouter_individus(enfants_selct)
    # todo : supprimer le surplus de la population dont le score est le plus bas.
    nb_iter += 1  # Si le nombre max d'itérations est atteint, on renvoie l'individu avec le score le plus élevé.
