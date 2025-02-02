# ALGO901_Algorithme_Genetique

## 1. Doc d'utilisation

La classe ```AlgoGenetique``` cherche le minimum d'une ```fonction``` f dans un intervalle noté ```ranges```. f doit être un objet héritant de la classe ```Performance``` et sept fonctions existent déjà : Schwefel, SixHumpCamelSix, F2, F6, F7, F8 et F9. L'intervalle noté ```ranges``` est une liste de liste, ex : [[a1, b1], [a2, b2]]. L'utilisateur doit saisir la taille de la population  ```taille_population``` et le nombre d'itérations ```nb_iter_max```. De plus l'algorithme demande un type de ```codage```, il est possible d'utiliser un ```CodageBinaire``` ou un ```CodageHexadecimal```, dans les 2 cas il faut spécifier [taille mantisse, taille exposant] (attention en codage binaire, ne pas prendre une taille d'exposant >= 11 bits, sinon problème de conversion si on se retrouve avec un exposant égal à1024). Il faut ensuite saisir un type de ```selection``` entre ```RoueDeLaFortune``` et ```Tournoi```, la sélection par tournoi prenant une probabilité p. L'utilisateur doit de plus spécifier le type de ```croisement``` utilisé par l'algorithme, il a le choix entre le ```CroisementSimple``` et le ```CroisementDouble```. Enfin, un type de mutation doit être choisi parmi la ```MutationParPermutation``` et ```MutationParFlipping``` (le dernier seulement pour le codage binaire).
 
Pour obtenir le minimum de la fonction dans l'intervalle choisi, il faut ensuite appeler la fonction ```alg.get_min()```, alg étant l'instance de la classe ```AlgoGenetique```. Cette fonction retourne les coordonnées trouvées par l'algo qui minimise f dans l'intervalle choisi ainsi que la valeur du minimum trouvé.

## 2. Benchmarks
### 2.1 Schwefel (R^2)
Avec les paramètres _ranges_=[-500, 500]^2, _taille\_population_=100, _nb\_iter\_max_=500, _codage_=```CodageBinaire([52, 10])```, _selection_=```RoueDeLaFortune()```, _croisement_=```CroisementDouble()``` et _mutation_=```MutationParPermutation(0.1)```. \
Nous trouvons un minimum en [420.008041359117, 419.9432208826837] qui a pour valeur -837.7167132529034 en 4.84s d'éxéction.
### 2.2 SixHumpCamelSix
Avec les paramètres _ranges_=[-5, 5]^2, _taille\_population_=100, _nb\_iter\_max_=500, _codage_=```CodageBinaire([52, 10])```, _selection_=```RoueDeLaFortune()```, _croisement_=```CroisementDouble()``` et _mutation_=```MutationParPermutation(0.1)```. \
Nous trouvons un minimum en [0.06562598207992915, -0.7044206810586376] qui a pour valeur -1.0290151956194344 en 2.37+s d'éxéction.
### 2.3 F2
### 2.4 F6
### 2.5 F7
### 2.6 F8
### 2.7 F9 (Schwefel R^10)
