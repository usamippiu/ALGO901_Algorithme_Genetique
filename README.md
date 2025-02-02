# ALGO901_Algorithme_Genetique

## 1. Doc d'utilisation

La classe ```AlgoGenetique``` cherche le minimum d'une ```fonction``` f dans un intervalle noté ```ranges```. f doit être un objet héritant de la classe ```Performance``` et sept fonctions existent déjà : Schwefel, SixHumpCamelSix, F2, F6, F7, F8 et F9. L'intervalle noté ```ranges``` est une liste de liste, ex : [[a1, b1], [a2, b2]]. L'utilisateur doit saisir la taille de la population  ```taille_population``` et le nombre d'itérations ```nb_iter_max```. De plus l'algorithme demande un type de ```codage```, il est possible d'utiliser un ```CodageBinaire``` ou un ```CodageHexadecimal```, dans les 2 cas il faut spécifier [taille mantisse, taille exposant] (attention en codage binaire, ne pas prendre une taille d'exposant >= 11 bits, sinon problème de conversion si on se retrouve avec un exposant égal à1024). Il faut ensuite saisir un type de ```selection``` entre ```RoueDeLaFortune``` et ```Tournoi```, la sélection par tournoi prenant une probabilité p. L'utilisateur doit de plus spécifier le type de ```croisement``` utilisé par l'algorithme, il a le choix entre le ```CroisementSimple``` et le ```CroisementDouble```. Enfin, un type de mutation doit être choisi parmi la ```MutationParPermutation``` et ```MutationParFlipping``` (le dernier seulement pour le codage binaire).

## 2. Benchmarks
