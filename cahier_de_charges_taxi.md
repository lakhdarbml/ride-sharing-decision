# Cahier de Charges – Système d’Assignation de Passagers à des Taxis

## 1. 🎯 Objectif du projet
Développer un système intelligent permettant d’affecter en temps réel des passagers à des taxis **sans destination pré-définie** (contrairement aux conducteurs particuliers).  
Le but est d’optimiser :  
- La **réduction du temps d’attente des passagers**.  
- La **minimisation des détours des taxis**.  
- La **maximisation du nombre de passagers servis**.  
- Le **coût opérationnel global** (distance parcourue, carburant, disponibilité).  

---

## 2. 🔑 Contraintes fonctionnelles
1. **Entrées principales** :  
   - Liste des taxis disponibles (position GPS en temps réel, capacité).  
   - Liste des passagers en attente (point de départ, destination souhaitée, heure de demande).  
   - Carte routière de la ville (graph routier : nœuds = intersections, arêtes = routes, pondérées par distance/temps).  

2. **Sorties attendues** :  
   - Affectation optimale taxi ↔ passager(s).  
   - Calcul de l’itinéraire proposé pour chaque taxi.  
   - Estimation du temps de trajet et du délai de prise en charge.  

3. **Fonctionnalités** :  
   - Localisation et mise à jour en temps réel.  
   - Gestion des capacités (ex. taxi peut transporter 3 passagers max).  
   - Réaffectation dynamique en cas de nouvelles demandes.  
   - Possibilité de prioriser certains critères : temps d’attente, distance, profit.  

---

## 3. 🔒 Contraintes non fonctionnelles
- **Performance** : l’algorithme doit répondre en temps quasi-réel (< 2 secondes).  
- **Scalabilité** : doit pouvoir gérer plusieurs centaines de taxis et passagers simultanément.  
- **Robustesse** : gérer les cas d’absence de chemin entre deux points.  
- **Interopérabilité** : système basé sur une API exploitable par une application mobile (passager et chauffeur).  

---

## 4. 📐 Contraintes du problème (modélisation)
1. Chaque taxi peut prendre **au maximum `capacity` passagers**.  
2. Chaque passager doit être servi **par un seul taxi**.  
3. Un taxi ne peut pas dépasser un **détour maximal autorisé** (ex. +20% de distance par rapport à un trajet direct).  
4. Les passagers doivent être servis **avant une deadline** (temps d’attente maximal).  
5. Objectif multicritère :  
   - Minimiser la **somme des distances parcourues**.  
   - Minimiser le **temps d’attente des passagers**.  
   - Maximiser le **taux de service** (passagers servis / total demandes).  

---

## 5. 🛠️ Approches possibles dans la littérature
- **Modèles exacts (optimisation combinatoire)** :  
  - Problème d’affectation bipartite (Hungarian Algorithm).  
  - Problème de flot maximum avec contraintes de capacité.  
  - Programmation linéaire entière (MILP).  

- **Heuristiques** :  
  - Algorithme glouton (taxi le plus proche).  
  - Recherche locale / Tabu Search.  
  - Algorithmes évolutionnaires.  

- **Méthodes avancées** :  
  - Reinforcement Learning pour l’affectation dynamique.  
  - Algorithmes basés sur le clustering (k-means pour regrouper les passagers proches).  

---

## 6. 📊 Indicateurs de performance
- Temps moyen d’attente des passagers.  
- Distance totale parcourue par les taxis.  
- Taux de remplissage des taxis.  
- Pourcentage de passagers servis.  
- Temps de calcul de l’algorithme.  
