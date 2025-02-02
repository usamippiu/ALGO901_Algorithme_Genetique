# ALGO901_Algorithme_Genetique

## 1. Doc d'utilisation

La classe ```AlgoGenetique``` cherche le minimum d'une ```fonction``` f dans un intervalle noté ```ranges```. f doit être un objet héritant de la classe ```Performance``` et sept fonctions existent déjà : Schwefel, SixHumpCamelSix, F2, F6, F7, F8 et F9. L'intervalle noté ```ranges``` est une liste de liste, ex : [[a1, b1], [a2, b2]]. L'utilisateur doit saisir la taille de la population  ```taille_population``` et le nombre d'itérations ```nb_iter_max```. De plus l'algorithme demande un type de ```codage```, il est possible d'utiliser un ```CodageBinaire``` ou un ```CodageHexadecimal```, dans les 2 cas il faut spécifier [taille mantisse, taille exposant] (attention en codage binaire, ne pas prendre une taille d'exposant >= 11 bits, sinon problème de conversion si on se retrouve avec un exposant égal à1024). Il faut ensuite saisir un type de ```selection``` entre ```RoueDeLaFortune``` et ```Tournoi```, la sélection par tournoi prenant une probabilité p. L'utilisateur doit de plus spécifier le type de ```croisement``` utilisé par l'algorithme, il a le choix entre le ```CroisementSimple``` et le ```CroisementDouble```. Enfin, un type de mutation doit être choisi parmi la ```MutationParPermutation``` et ```MutationParFlipping``` (le dernier seulement pour le codage binaire).
 
Pour obtenir le minimum de la fonction dans l'intervalle choisi, il faut ensuite appeler la fonction ```alg.get_min()```, alg étant l'instance de la classe ```AlgoGenetique```. Cette fonction retourne les coordonnées trouvées par l'algo qui minimise f dans l'intervalle choisi ainsi que la valeur du minimum trouvé.

## 2. Benchmarks
### 2.1 Schwefel (R^2)
Avec les paramètres _ranges_=[-500, 500]^2, _taille\_population_=100, _nb\_iter\_max_=500, _codage_=```CodageBinaire([52, 10])```, _selection_=```RoueDeLaFortune()```, _croisement_=```CroisementDouble()``` et _mutation_=```MutationParPermutation(0.1)```. \
Nous trouvons un minimum en (420.008041359117, 419.9432208826837) qui a pour valeur -837.7167132529034 en 4.84s d'éxéction.
### 2.2 SixHumpCamelSix
Avec les paramètres _ranges_=[-5, 5]^2, _taille\_population_=100, _nb\_iter\_max_=500, _codage_=```CodageBinaire([52, 10])```, _selection_=```RoueDeLaFortune()```, _croisement_=```CroisementSimple()``` et _mutation_=```MutationParPermutation(0.1)```. \
Nous trouvons un minimum en (0.06562598207992915, -0.7044206810586376) qui a pour valeur -1.0290151956194344 en 2.37s d'éxéction.
### 2.3 F2
Avec les paramètres _ranges_=[-2.048, 2.048]^2, _taille\_population_=100, _nb\_iter\_max_=500, _codage_=```CodageBinaire([52, 10])```, _selection_=```RoueDeLaFortune()```, _croisement_=```CroisementSimple()``` et _mutation_=```MutationParPermutation(0.1)```. \
Nous trouvons un minimum en (0.9320810161474107, 0.8722344805281042) qui a pour valeur 0.0058097746238172255 en 2.36s d'éxéction.
### 2.4 F6
Avec les paramètres _ranges_=[-100, 100]^2, _taille\_population_=100, _nb\_iter\_max_=500, _codage_=```CodageHexadecimal([52, 10])```, _selection_=```RoueDeLaFortune()```, _croisement_=```CroisementSimple()``` et _mutation_=```MutationParPermutation(0.1)```. \
Nous trouvons un minimum en (3.3239639297148236e-144, 5.142668110954431e-144) qui a pour valeur 0.0 en 4.18s d'éxéction.
### 2.5 F7
Avec les paramètres _ranges_=[-5.12, 5.12]^20, _taille\_population_=100, _nb\_iter\_max_=500, _codage_=```CodageBinaire([52, 10])```, _selection_=```RoueDeLaFortune()```, _croisement_=```CroisementSimple()``` et _mutation_=```MutationParPermutation(0.1)```. \
Nous trouvons un minimum en (-3.0339514789280263e-144, -3.6777666486344104e-144) qui a pour valeur 0.023795169715223857 en 8.02s d'éxéction.
### 2.6 F8
Avec les paramètres _ranges_=[-600, 600]^10, _taille\_population_=100, _nb\_iter\_max_=500, _codage_=```CodageBinaire([52, 10])```, _selection_=```Tournoi(0.8)```, _croisement_=```CroisementSimple()``` et _mutation_=```MutationParFlipping(0.1)```. \
Nous trouvons un minimum en (8.590842397580303e-38, -2.054465568928433e-104, 21.280533354627053, -4.650317313408654, -1.370408706591785e-152, -9.137999087135719e-29, -6.559560404557348, -5.160946493404783e-116, -1.4477094438482678e-142, -2.6250979356259735e-76) qui a pour valeur 0.6103836729369639 en 49.49s d'éxéction.
### 2.7 F9 (Schwefel R^10)
Avec les paramètres _ranges_=[-5.12, 5.12]^20, _taille\_population_=100, _nb\_iter\_max_=500, _codage_=```CodageBinaire([52, 10])```, _selection_=```RoueDeLaFortune()```, _croisement_=```CroisementSimple()``` et _mutation_=```MutationParPermutation(0.1)```. \
Nous trouvons un minimum en 420.743319050752, 415.9955375933257, 419.724546194961, 415.98658601067484, 420.8796317860739, 420.9393254799759, 420.7142584518989, 421.40430582873915, 415.9673927193063, 420.9217024367299) qui a pour valeur -4170.214279755621 en 45.05s d'éxéction.
