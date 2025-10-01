# 🚕 Ride-Matching Intelligent pour Taxis (Aide à la Décision)

## 📌 1. Introduction
Le projet vise à développer un système d’aide à la décision pour l’assignation de passagers aux taxis disponibles en milieu urbain.  
Contrairement aux taxis classiques, ce modèle ne suppose pas de destination fixe du conducteur mais optimise l’affectation des passagers afin de :  
- Minimiser le temps d’attente.  
- Maximiser l’utilisation des taxis.  
- Réduire la congestion et les kilomètres parcourus à vide.  

---

## 📌 2. Analyse du problème
- **Contraintes principales** :  
  - Capacité des taxis.  
  - Distance ou temps maximal de détour accepté.  
  - Respect de l’ordre de prise en charge.  
- **Critères de performance** :  
  - Temps moyen d’attente.  
  - Taux de satisfaction des passagers.  
  - Kilomètres parcourus par taxi.  

---

## 📌 3. Revue de littérature
Le problème étudié est lié à :  
- **Taxi Dispatch Problem (TDP)**.  
- **Dial-a-Ride Problem (DARP)**.  
- **Dynamic Ride-Matching Problem (DRMP)**.  

Les approches incluent :  
- Graphes et plus courts chemins (Dijkstra, A*).  
- Optimisation combinatoire (MILP, heuristiques).  
- Intelligence Artificielle (matching biparti, RL).  

---

## 📌 4. Modélisation mathématique
- **Ensemble des taxis** : \( T = \{t_1, \dots, t_m\} \).  
- **Ensemble des passagers** : \( P = \{p_1, \dots, p_n\} \).  
- **Variable de décision** :  
  - \( x_{ij} = 1 \) si le passager \( p_j \) est affecté au taxi \( t_i \).  
- **Contraintes** :  
  - Chaque passager au plus dans un taxi.  
  - Capacité respectée.  
  - Détour maximal limité.  
- **Objectif** : minimiser le temps total (trajet + attente).  

---

## 📌 5. Données nécessaires
- Graphe routier via **OpenStreetMap** (OSMnx).  
- Positions GPS des taxis.  
- Positions GPS des passagers.  
- Capacités des taxis.  
- Paramètres de détour max.  

---

## 📌 6. Méthodologie
1. Import des données (graphes routiers OSM).  
2. Modélisation du problème comme un **matching biparti avec contraintes**.  
3. Algorithmes :  
   - Exact (MILP avec OR-Tools).  
   - Heuristique (greedy, Hungarian Algorithm).  
   - IA (apprentissage par renforcement).  
4. Simulation de scénarios de demande.  
5. Évaluation des performances.  

---

## 📌 7. Développement
- **Backend** : Python (NetworkX, OSMnx, OR-Tools).  
- **Frontend** : Flask/Django (ou React).  
- **BDD** : SQLite ou PostgreSQL.  
- **Tests unitaires** : pytest.  

---

## 📌 8. Résultats attendus
- Visualisation des trajets sur carte.  
- Statistiques sur satisfaction passagers et km parcourus.  
- Comparaison des méthodes (exactes vs heuristiques).  

---

## 📌 9. Conclusion
Le projet vise à proposer une solution innovante d’affectation des passagers aux taxis en milieu urbain, avec des perspectives vers une intégration en temps réel.  

---
