from Individu import Individu
from Coordonnee import Coordonnee

class Population:
    def __init__(self, nombreMax, fonctionPerformance, individus = []):
        self.individus = individus
        self.nombreMax = nombreMax
        self.fonctionPerformance = fonctionPerformance # Objet = fonction qu'on va utiliser pour évaluer la population
    
    # Ajouter des individus dans la population, prend en parametre une liste d'individus  
    def ajouter_individus(self, individus):
        if len(self.individus) + len(individus) <= self.nombreMax: # peut on bien ajouter la liste ? Si oui :
            # on calcule le score des individus et on les ajoute
            [individu.set_score_performance(self) for individu in individus if individu.scorePerformance is None]
            self.individus.extend(individus)
        else:
            print("Population maximale atteinte.")
            
    # Supprimer une liste d'individus en paramètre parmi la population ( self.individus )
    def supprimer_individus(self, individus):
        for individu in individus:
            if individu in self.individus:
                self.individus.remove(individu)
            else:
                print(f"L'individu {individu} n'est pas dans la population.")
    
    # Affiche les individus dans la population
    def afficher_population(self):
        if self.individus:
            print("Il y a", self.nombreMax, "individus dans la population.")
            print("Ce sont les suivants:")
            for individu in self.individus:
                print(individu)
        else:
            print("La population est vide.")

    # On va générer une population d'individus aléatoirement
    def generer_population(self, fenetres, typeCodage):
        # On a besoin d'une methode qui init un individu et on fait une boucle jusqu'à atteindre nb max, puis on les ajoute
        # on genere des coordonnees aleatoires , on evalue les coordonnees, on les code et on génère l'individu avec
        n=0       
        coordonnees = []
        
        # On genere ensuite des valeurs de coordonnees
        while(n < len(fenetres)):         # dimension du travail
            coordonnee_alea = Coordonnee(fenetres[n], typeCodage)
            coordonnee_alea.set_valeur_coordonnee()
            coordonnees.append(coordonnee_alea)
            n += 1

        n=0
        individus = []
        # On genere un individu aléatoirement
        while(n <= self.nombreMax):
            individu_alea = Individu(coordonnees[n])
            individu_alea.set_score_performance(self)
            individus.append(individu_alea)
            n += 1
            
        self.ajouter_individus(individus)
