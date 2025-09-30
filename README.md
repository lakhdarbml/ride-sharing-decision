# 🚗 Système d’aide à la décision pour l’optimisation des itinéraires et du covoiturage  

## 📌 Contexte  
La mobilité urbaine pose aujourd’hui des défis majeurs : congestion, pollution, perte de temps.  
Ce projet propose une solution basée sur **l’optimisation des itinéraires** et le **matching passagers–conducteurs** afin de rendre le covoiturage plus efficace et durable.  

---

## 🎯 Objectifs  
- Calculer l’**itinéraire le plus court** ou le plus rapide pour un conducteur.  
- Optimiser l’**affectation passagers-véhicules** pour minimiser les détours.  
- Fournir une **aide à la décision** avec visualisation des trajets.  

---

## ⚙️ Fonctionnalités  
✅ Inscription des conducteurs et passagers (point de départ, destination, nb de places).  
✅ Calcul d’itinéraires optimaux avec **Dijkstra / A***.  
✅ Optimisation du **matching passagers–conducteurs** (VRP / Hungarian Algorithm).  
✅ Visualisation sur carte interactive (OpenStreetMap / Folium).  
✅ Statistiques sur les trajets (distance totale, gain de temps, CO₂ économisé).  

---

## 🛠️ Outils & Technologies  
- **Backend** : Python (Flask ou Django)  
- **Algorithmes** : NetworkX, OR-Tools, Dijkstra, A*  
- **Frontend** : React.js ou Tkinter (selon choix)  
- **Cartographie** : Folium / Leaflet.js (OpenStreetMap)  
- **Base de données** : SQLite ou PostgreSQL  

---

## 📂 Structure du projet  
├── backend/ # API & algorithmes d’optimisation
├── frontend/ # Interface utilisateur
├── data/ # Jeux de données (points GPS, utilisateurs, trajets)
├── docs/ # Documentation & cahier des charges
├── tests/ # Scénarios de test
└── README.md # Présentation du projet