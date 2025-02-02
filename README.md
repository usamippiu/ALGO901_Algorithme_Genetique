# ALGO901_Algorithme_Genetique

## 1. Doc d'utilisation

La classe ```AlgoGenetique``` cherche le minimum d'une ```fonction``` f dans un intervalle noté ```ranges```. f doit être un objet héritant de la classe ```Performance``` et sept fonctions existent déjà : Schwefel, SixHumpCamelSix, F2, F6, F7, F8 et F9. L'intervalle noté ```ranges``` est une liste de liste, ex : [[a1, b1], [a2, b2]]. L'utilisateur doit aussi saisir la taille de la population  ```taille_population``` et le nombre d'iterations ```nb_iter_max```. De plus l'algorithme demande un type de ```codage```, il est possible d'utilisé un ```CodageBinaire``` ou un ```CodageHexadecimal``` (Attention en codage binaire, ne pas prendre un exposant >= 11 bits, sinon problème de conversion si on se retrouve avec un exposant = 1024)

## 2. Benchmarks
