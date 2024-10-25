class Population:
    def __init__(self, nombreMax, fonctionPerformance):
        self.individus = []
        self.nombreMax = nombreMax
        self.fonctionPerformance = fonctionPerformance # Objet = fonction qu'on va utiliser pour évaluer la population
    
    # Ajouter des individus dans la population, prend en parametre une liste d'individus  
    def ajouter_individus(self, individus):
        if len(self.individus) + len(individus) <= self.nombreMax:
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
    # où l'individu est un objet comportant des coordonnees dans R^n, leurs valeurs, comprises entre les valeurs de la fenêtre)
    def generer_population(self, nombreMax):
        # On a besoin d'une methode qui init un individu et on fait une boucle jusqu'à atteindre nb max, puis on les ajoute
       # on genere des coordonnees aleatoires , on evalue les coordonnees, on les code et on génère l'individu avec
        pass
    
