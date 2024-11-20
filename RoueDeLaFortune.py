import random
import math

from SelectionParents import SelectionParents as Selection
from Individu import Individu
from Coordonnee import Coordonnee
from Fenetre import Fenetre
from CodageBinaire import CodageBinaire
from Population import Population
from Carre import F


# Cette méthode de sélection consiste à tirer des individus pour minimiser une fonction.
# On tire une valeur cible aléatoirement entre 0 et la somme des performances ;
# on initialise une variable perf = 0 qui sert de compteur cumulatif des performances de chaque individu :
# on l'initialise à 0 car on veut calculer la contribution de chaque individu à partir de 0 ;
# elle calcule la somme des inverses des valeurs de performances (pour minimiser la fonction), jusqu'à atteindre la valeur cible ;
# on sélectionne l'individu qui vérifie cette condition.
# Ainsi, chaque individu occupe une proportion de la roue, proportionnellement à son score de performance.
# Atteindre la valeur cible signifie qu'on a trouvé l'individu sélectionné.

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
        # Calcul de la performance totale
        total_performance = self.calcule_total_performance()

        # Tirage d'un nombre aléatoire entre 0 et la somme totale des performances en valeur absolue
        valeurAleatoire = 1/random.uniform(0, abs(total_performance))
        
        # Parcours de la population et sélection de l'individu correspondant
        perf = 0
        scoreIndividu = 0
        for individu in self.population.individus:
            # On utilise l'inverse de la fonction pour minimiser : les proportions les plus faibles deviennent les plus grandes
            individu.scorePerformance = individu.set_score_performance(self.population) # calcule None ...
            scoreIndividu = individu.scorePerformance
            print("score =", individu.scorePerformance)
            perf += 1/(scoreIndividu + 1e-9)        ## Comment est évaluée la performance de l'individu ? ##
            if perf >= valeurAleatoire:
                return individu, perf




    def selection_parents(self):
        # total_performance = self.calcule_total_performance()

        parent1 = self.roue_de_la_fortune()
        parent2 = self.roue_de_la_fortune()

        while parent1 == parent2:
            parent2 = self.roue_de_la_fortune()

        return parent1, parent2
    

if __name__=="__main__":
    f = F('f')
    
    fenetreX = Fenetre(-10,10,'x')
    codage = CodageBinaire([32,6])
    coordonneeX1 = Coordonnee(fenetreX, codage, f.eval(1))
    x1 = Individu(coordonneeX1)
    #x1.scorePerformance = f.eval(1)
    coordonneeX2 = Coordonnee(fenetreX, codage, f.eval(2))
    x2 = Individu(coordonneeX2)
    #x2.scorePerformance = f.eval(2)
    coordonneeX3 = Coordonnee(fenetreX, codage, f.eval(3))
    x3 = Individu(coordonneeX3)
    #x3.scorePerformance = f.eval(3)
    # coordonneeX4 = Coordonnee(fenetreX, codage)
    # x4 = Individu(coordonneeX4)
    # x4.scorePerformance = f.eval(4)
    # coordonneeX5 = Coordonnee(fenetreX, codage)
    # x5 = Individu(coordonneeX5)
    # x5.scorePerformance = f.eval(5)

    
    population = Population(50, f)
    population.ajouter_individus([x1,x2,x3])


    methode = RoueDeLaFortune(population)
    print("performance totale = ",methode.calcule_total_performance())
    methode.selection_parents()
