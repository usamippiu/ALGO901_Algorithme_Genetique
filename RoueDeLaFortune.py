import random

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
        total_perf = sum(1/individu.scorePerformance for individu in self.population.individus)
        return total_perf


    def roue_de_la_fortune(self):
        # Calcul de la performance totale
        total_performance = self.calcule_total_performance()

        # Tirage d'un nombre aléatoire entre 0 et la somme totale des performances en valeur absolue
        valeurAleatoire = random.uniform(0, abs(total_performance))
        
        # Parcours de la population et sélection de l'individu correspondant
        perf = 0
        scoreIndividu = 0
        for individu in self.population.individus:
            # On utilise l'inverse de la fonction pour minimiser : les proportions les plus faibles deviennent les plus grandes
            individu.set_score_performance(self.population)
            scoreIndividu = individu.scorePerformance
            print("score =", individu.scorePerformance)
            perf += 1/(scoreIndividu + 1e-9)
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
    f = F('f')  # fonction carre
    
    fenetreX = Fenetre(-10,10,'x')
    codage = CodageBinaire([32,6])
    coordonneeX1 = Coordonnee(fenetreX, codage, 1)
    x1 = Individu([coordonneeX1])
    #x1.scorePerformance = f.eval(1)
    coordonneeX2 = Coordonnee(fenetreX, codage, 2)
    x2 = Individu([coordonneeX2])
    #x2.scorePerformance = f.eval(2)
    coordonneeX3 = Coordonnee(fenetreX, codage, 3)
    x3 = Individu([coordonneeX3])


    population = Population(50, f)
    population.ajouter_individus([x1,x2,x3])


    methode = RoueDeLaFortune(population)
    print("performance totale = ",methode.calcule_total_performance())
    listeParents = methode.selection_parents()
    print([parent[0].coordonnees[0].valeur for parent in listeParents])