from AlgoGenetique import *

# Paramètres de l'algorithme :
alg = AlgoGenetique(
    fonction=F9(),
    ranges=[[-500, 500], [-500, 500], [-500, 500], [-500, 500], [-500, 500], [-500, 500], [-500, 500], [-500, 500],
        [-500, 500], [-500, 500], ],
    taille_population=100,
    nb_iter_max=100,
    codage=CodageBinaire([52, 10]),
    selection=RoueDeLaFortune(),
    croisement=CroisementSimple(),
)

# Exécution de l'algorithme :
res, value = alg.get_min()

# Affichage des résultats :
print(f"Coordonnées de l'individu minimal trouvé : {res[0], res[1]}")
print(f"Score de performance de l'individu minimal trouvé : {value}")
