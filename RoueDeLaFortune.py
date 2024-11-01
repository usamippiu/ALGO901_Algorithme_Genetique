import random
import math

from Selection import Selection
from Individu import Individu
from Coordonnee import Coordonnee
from Fenetre import Fenetre
from CodageBinaire import CodageBinaire
from Population import Population
from Carre import F


# Avec cette méthode, chaque valeur d'une fonction occupe une certaine proportion de la roue.
# Il s'agit de tirer des valeurs (individus) en fonction de la proportion d'occupation de la roue.
# On calcule la performance totale (total_performance) de l'ensemble des évaluations des valeurs par la fonction.
# Chaque individu a une proportion d'occupation de la roue (valeur/total_performance).
# On tire un nombre aléatoirement.
# On regarde si l'inverse de l'évaluation de l'individu par la fonction est supérieure au nombre aléatoirement tiré.
# Cela permet de choisir suivant des proportions d'occupation de la roue, et de minimiser

class RoueDeLaFortune(Selection):
    def __init__(self, population):
        super().__init__(population)

    def calcule_total_performance(self):
        # for i in range(len(self.population.individus)):
        #     total_perf = sum(scoreperformance for scoreperformance in self.population.individus[i].scorePerformance) # somme le score de performance de tout les individus de la population en paramètre de l'objet RoueDeLaFortune
        total_perf = sum(individu.scorePerformance for individu in self.population.individus)
        total_perf = 1/total_perf
        return total_perf

    # def liste_fitness(self):
    #     # tri des valeurs des individus par ordre croissant
    #     liste_valeurs = [self.population.individus[i].coordonnees.valeur for i in range(len(self.population.individus))]
    #     valeurs_triees = sorted(liste_valeurs)  ## Error : '<' not supported between instances of 'Individu' and 'Individu' ##
    #     liste_cumulee = []
    #     total = 0
    #     # ajout des valeurs cumulées des fitness des individus
    #     for valeur in valeurs_triees:
    #         total += valeur
    #         liste_cumulee.append(total)
    #     return liste_cumulee

    def roue_de_la_fortune(self):
        # total_performance = self.calcule_total_performance()

        # # proportion_roue = [self.population.individus[i]/total_performance for i in range(len(self.population.individus))]

        # # Liste des valeurs cumulées des fitness et des valeurs des individus
        # listeFitness = self.liste_fitness()

        # # Tirage d'un nombre aléatoire entre 0 et total_performance
        # nombreAlea = random.uniform(0, abs(total_performance))

        # for i in range(len(listeFitness)):
        #     if nombreAlea >= listeFitness[i-1] and nombreAlea < listeFitness[i]:
        #         valeur = self.population.individus[i-1]

        # return valeur

        # Calcul de la performance totale
        total_performance = self.calcule_total_performance()

        # Tirage d'un nombre aléatoire entre 0 et la somme totale des performances en valeur absolue
        valeurAleatoire = random.uniform(0, abs(total_performance))
        
        # Parcours de la population et sélection de l'individu correspondant
        perf = 0
        for individu in self.population.individus:
            # On utilise l'inverse de la fonction pour minimiser : les proportions les plus faibles deviennent les plus grandes
            individu.scorePerformance = individu.set_score_performance(self.population) # calcule None ...
            scoreIndividu = individu.scorePerformance
            print("score =", individu.scorePerformance)
            perf += 1 / (scoreIndividu + 1e-9)        ## Comment est évaluée la performance de l'individu ? ##
            if perf >= valeurAleatoire:
                return individu, perf
            
# Cette méthode de sélection consiste à tirer des individus pour minimiser une fonction.
# On tire une valeur cible aléatoirement entre 0 et la somme des performances ;
# on initialise une variable perf = 0 qui sert de compteur cumulatif des performances de chaque individu :
# on l'initialise à 0 car on veut calculer la contribution de chaque individu à partir de 0 ;
# elle calcule la somme des inverses des valeurs de performances (pour minimiser la fonction), jusqu'à atteindre la valeur cible ;
# on sélectionne l'individu qui vérifie cette condition.
# Ainsi, chaque individu occupe une proportion de la roue, proportionnellement à son score de performance.
# Atteindre la valeur cible signifie qu'on a trouvé l'individu sélectionné.

        

        # # Parcours de la population et sélection de l'individu choisi
        # perf = 0
        # #for individu in self.population.individus:
        # for i in range(len(self.population.individus)):
        #     # calcul de la performance de l'individu (évaluation par la fonction)
        #     perf += self.population.individus[i].scorePerformance

        #     # comparaison de l'évaluation avec le nombre aléatoire tiré initialement :
        #     # si sa valeur est supérieure ou égale au nombre, on le retourne
        #     if perf >= nombreAlea:
        #         return self.population.individus[i].coordonnees.valeur


    def selection_parents(self):
        # total_performance = self.calcule_total_performance()

        parent1 = self.roue_de_la_fortune()
        parent2 = self.roue_de_la_fortune()

        while parent1 == parent2:
            parent2 = self.roue_de_la_fortune()

        return parent1, parent2
    

if __name__=="__main__":
    f = F('f')
    def g(x):
        return math.sqrt(x)
    
    fenetreX = Fenetre(-10,10,'x')
    codage = CodageBinaire([32,6])
    coordonneeX1 = Coordonnee(1, fenetreX, codage)
    x1 = Individu(coordonneeX1)
    x1.scorePerformance = f.eval(1)
    coordonneeX2 = Coordonnee(2, fenetreX, codage)
    x2 = Individu(coordonneeX2)
    x2.scorePerformance = f.eval(2)
    coordonneeX3 = Coordonnee(3, fenetreX, codage)
    x3 = Individu(coordonneeX3)
    x3.scorePerformance = f.eval(3)
    coordonneeX4 = Coordonnee(4, fenetreX, codage)
    x4 = Individu(coordonneeX4)
    x4.scorePerformance = f.eval(4)
    coordonneeX5 = Coordonnee(5, fenetreX, codage)
    x5 = Individu(coordonneeX5)
    x5.scorePerformance = f.eval(5)

    
    population = Population(50, f)
    population.ajouter_individus([x1,x2,x3,x4,x5])


    methode = RoueDeLaFortune(population)
    print("performance totale = ",methode.calcule_total_performance())

    print(methode.selection_parents())