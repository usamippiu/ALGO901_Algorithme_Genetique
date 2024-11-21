from Individu import Individu
from Coordonnee import Coordonnee

class Population:
    def __init__(self, nombreMax, fonctionPerformance, individus = None):
        if individus is None :
            self.individus = []
        else:
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
                print()
                print("Coordonnées de l'individu:" , [coord.valeur for coord in individu.coordonnees])
                print("Score de l'individu:" ,individu.scorePerformance )

        else:
            print("La population est vide.")

    # On va générer une population d'individus aléatoirement
    def generer_population(self, fenetres, typeCodage):
        # On a besoin d'une methode qui init un individu et on fait une boucle jusqu'à atteindre nb max, puis on les ajoute
        # on genere des coordonnees aleatoires , on evalue les coordonnees, on les code et on génère l'individu avec  
        
        for n in range(self.nombreMax):
            
            coordonnees = []
            # On genere ensuite des valeurs de coordonnees # On a n fenetres donc n coordonnées, on a besoin de les associer à un individu
            for i in range(len(fenetres)):         # dimension du travail
                coordonnee_alea = Coordonnee(fenetres[i], typeCodage)
                # coordonnee_alea.set_valeur_coordonnee(fenetres[i])
                coordonnees.append(coordonnee_alea)
                
            # On genere un individu aléatoirement
            individu_alea = Individu(coordonnees)
            individu_alea.set_score_performance(self)
            self.individus.append(individu_alea)

    def lf_individu_minimal(self):
        if not self.individus:
            return None
        
        # Utiliser la fonction min avec une clé pour comparer les scores
        individu_min = min(self.individus, key=lambda individu: individu.scorePerformance)
        
        return individu_min