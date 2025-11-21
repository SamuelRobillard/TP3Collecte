# TP3 - Collecte et interprétation de données

## Membres de l'équipe 

- Bradley Leneus
- Samuel Robillard
- Alexandre Rusenov

## Description
Ce travail pratique consiste en une étude de cas basée sur des données réelles de Yelp, une plateforme où les utilisateurs évaluent et commentent divers restaurants. L’objectif est de construire un dataset intégré en combinant plusieurs tables du jeu de données Yelp (restaurants, avis, utilisateurs, services, horaires, catégories, etc.) afin d’extraire des indicateurs clés tels que le ratio d’avis favorables, le nombre total d’avis, la popularité ou encore la présence de chaînes. 

À partir de ce dataset enrichi, l’équipe doit réaliser deux visualisations : une statique et une interactive, chacune accompagnée d’un titre clair, d’axes bien définis et d’une interprétation de 3 à 5 lignes, tel qu’exigé dans le document du TP. L’analyse finale doit soulever des observations pertinentes sur les tendances observées dans les données (qualité, satisfaction, activité des restaurants, etc.).

Le travail met également l’accent sur la qualité du code, la rigueur dans le nettoyage et l’intégration des données, la lisibilité du notebook ainsi que la clarté du README. Enfin, chaque membre de l’équipe doit contribuer à une partie spécifique (préparation des données, intégration des indicateurs, visualisations et interprétation), conformément à la répartition recommandée dans l'énoncé.

##  Installation 

### Prérequis
- Python 3.7+
- Pip

### Dépendances
```bash
pip install pandas numpy matplotlib plotly
```

### Exécution du notebook
Placez le fichier restaurants_features.csv dans le même dossier que le notebook

## Séparation des tâches

### Samuel

La lecture des csv de base et la création du data frame personnalité. Cela inclue la sélection des données des csv, les traîtements des données et les jointures nécessaires. 

### Bradley
Réalisation du graphique statique, incluant la préparation des données et la construction de la visualisation.
Rédaction de l’analyse et de l’interprétation associées au graphique.
Prise en charge de la remise du travail, avec vérification de la conformité aux exigences.
Contribution à l’amélioration du README, afin d’en clarifier la structure et le contenu.
Travail sur la clarté du notebook, notamment par l’ajout de cellules explicatives pour faciliter la compréhension du code.
### Alexandre
La création d’un graphique interactif permettant d’afficher le top 10 des restaurants par ville selon le nombre d’avis positifs. L’utilisateur peut sélectionner une ville à partir d’un menu déroulant, et le graphique se met automatiquement à jour. L’analyse et l’interprétation du graphique ont également été rédigées, conformément aux exigences du PDF, afin de mettre en évidence les tendances observées et la signification des données.
