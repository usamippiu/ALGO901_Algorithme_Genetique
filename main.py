from Fenetre import Fenetre
from Population import Population
from RoueDeLaFortune import RoueDeLaFortune
from Tournoi import Tournoi
from CodageBinaire import CodageBinaire
from CodageHexadecimal import CodageHexadecimal
from Schwefel import Schwefel
from F2 import F2
from F6 import F6
from F7 import F7
from F8 import F8
from F9 import F9
from SixHumpCamelSix import SixHumpCamelSix
from CroisementSimple import CroisementSimple
from CroisementDouble import CroisementDouble
from MutationParPermutation import MutationParPermutation
from MutationParFlipping import MutationParFlipping
from AlgoGenetique import AlgoGenetique

import time

# Test Fonction Schwefel
# Paramètres de l'algorithme :
alg = AlgoGenetique(
    fonction=Schwefel(),
    ranges=[[-500, 500], [-500, 500]],
    taille_population=100,
    nb_iter_max=500,
    codage=CodageBinaire([52, 10]),
    selection=RoueDeLaFortune(),
    croisement=CroisementDouble(),
    mutation=MutationParPermutation(0.1),
)

# Exécution de l'algorithme :
start_all = time.perf_counter()
start_func = time.perf_counter()
res, value = alg.get_min()

# Affichage des résultats :
print("------------------- Schwefel (R^2) -------------------")
print(
    f"Coordonnées de l'individu minimal trouvé : {res[0], res[1]} en {round(time.perf_counter() - start_func, 2)}s"
)
print(f"Score de performance de l'individu minimal trouvé : {value}")

# Test Fonction SixHumpCamelSix
# Paramètres de l'algorithme :
alg = AlgoGenetique(
    fonction=SixHumpCamelSix(),
    ranges=[[-5, 5], [-5, 5]],
    taille_population=100,
    nb_iter_max=500,
    codage=CodageBinaire([52, 10]),
    selection=RoueDeLaFortune(),
    croisement=CroisementSimple(),
    mutation=MutationParPermutation(0.1),
)

# Exécution de l'algorithme :
start_func = time.perf_counter()
res, value = alg.get_min()

# Affichage des résultats :
print("------------------- SixHumpCamelSix -------------------")
print(
    f"Coordonnées de l'individu minimal trouvé : {res[0], res[1]} en {round(time.perf_counter() - start_func, 2)}s"
)
print(f"Score de performance de l'individu minimal trouvé : {value}")

# Test Fonction F2
# Paramètres de l'algorithme :
alg = AlgoGenetique(
    fonction=F2(),
    ranges=[[-2.048, 2.048], [-2.048, 2.048]],
    taille_population=100,
    nb_iter_max=500,
    codage=CodageBinaire([52, 10]),
    selection=RoueDeLaFortune(),
    croisement=CroisementSimple(),
    mutation=MutationParPermutation(0.1),
)

# Exécution de l'algorithme :
start_func = time.perf_counter()
res, value = alg.get_min()

# Affichage des résultats :
print("------------------- F2 -------------------")
print(
    f"Coordonnées de l'individu minimal trouvé : {res[0], res[1]} en {round(time.perf_counter() - start_func, 2)}s"
)
print(f"Score de performance de l'individu minimal trouvé : {value}")

# Test Fonction F6
# Paramètres de l'algorithme :
alg = AlgoGenetique(
    fonction=F6(),
    ranges=[[-100, 100], [-100, 100]],
    taille_population=100,
    nb_iter_max=500,
    codage=CodageHexadecimal([52, 10]),
    selection=RoueDeLaFortune(),
    croisement=CroisementSimple(),
    mutation=MutationParPermutation(0.1),
)

# Exécution de l'algorithme :
start_func = time.perf_counter()
res, value = alg.get_min()

# Affichage des résultats :
print("------------------- F6 -------------------")
print(
    f"Coordonnées de l'individu minimal trouvé : {res[0], res[1]} en {round(time.perf_counter() - start_func, 2)}s"
)
print(f"Score de performance de l'individu minimal trouvé : {value}")

# Test Fonction F7
# Paramètres de l'algorithme :
alg = AlgoGenetique(
    fonction=F7(),
    ranges=[
        [-5.12, 5.12],
        [-5.12, 5.12],
        [-5.12, 5.12],
        [-5.12, 5.12],
        [-5.12, 5.12],
        [-5.12, 5.12],
        [-5.12, 5.12],
        [-5.12, 5.12],
        [-5.12, 5.12],
        [-5.12, 5.12],
    ],
    taille_population=100,
    nb_iter_max=500,
    codage=CodageBinaire([52, 10]),
    selection=RoueDeLaFortune(),
    croisement=CroisementSimple(),
    mutation=MutationParPermutation(0.1),
)

# Exécution de l'algorithme :
start_func = time.perf_counter()
res, value = alg.get_min()

# Affichage des résultats :
print("------------------- F7 -------------------")
print(
    f"Coordonnées de l'individu minimal trouvé : {res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7], res[8], res[9]} en {round(time.perf_counter() - start_func, 2)}s"
)
print(f"Score de performance de l'individu minimal trouvé : {value}")

# Test Fonction F8
# Paramètres de l'algorithme :
alg = AlgoGenetique(
    fonction=F8(),
    ranges=[
        [-600, 600],
        [-600, 600],
        [-600, 600],
        [-600, 600],
        [-600, 600],
        [-600, 600],
        [-600, 600],
        [-600, 600],
        [-600, 600],
        [-600, 600],
    ],
    taille_population=100,
    nb_iter_max=500,
    codage=CodageBinaire([52, 10]),
    selection=Tournoi(0.8),
    croisement=CroisementSimple(),
    mutation=MutationParFlipping(0.1),
)

# Exécution de l'algorithme :
start_func = time.perf_counter()
res, value = alg.get_min()

# Affichage des résultats :
print("------------------- F8 -------------------")
print(
    f"Coordonnées de l'individu minimal trouvé : {res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7], res[8], res[9]} en {round(time.perf_counter() - start_func, 2)}s"
)
print(f"Score de performance de l'individu minimal trouvé : {value}")

# Test fonction F9 (Schwefel 10x10)
# Paramètres de l'algorithme :
alg = AlgoGenetique(
    fonction=F9(),
    ranges=[
        [-500, 500],
        [-500, 500],
        [-500, 500],
        [-500, 500],
        [-500, 500],
        [-500, 500],
        [-500, 500],
        [-500, 500],
        [-500, 500],
        [-500, 500],
    ],
    taille_population=100,
    nb_iter_max=500,
    codage=CodageBinaire([52, 10]),
    selection=RoueDeLaFortune(),
    croisement=CroisementSimple(),
    mutation=MutationParPermutation(0.1),
)

# Exécution de l'algorithme :
start_func = time.perf_counter()
res, value = alg.get_min()

# Affichage des résultats :
print("------------------- Schwefel (R^10) -------------------")
print(
    f"Coordonnées de l'individu minimal trouvé : {res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7], res[8], res[9]} en {round(time.perf_counter() - start_func, 2)}s"
)
print(f"Score de performance de l'individu minimal trouvé : {value}")

print(f"Temps total écoulé : {time.perf_counter() - start_all}")
