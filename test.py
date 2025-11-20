import pandas as pd
import numpy as np

# Chargement des fichiers CSV
tableRestaurants = pd.read_csv('restaurants.csv')
tableAvis = pd.read_csv('avis.csv')
tableCategories = pd.read_csv('categories.csv')
tableCheckin = pd.read_csv('checkin.csv')
tableHoraire = pd.read_csv('horaires.csv')
tableServices = pd.read_csv('services.csv')
tableUtilisateurs = pd.read_csv('utilisateurs.csv')

# Création du DataFrame ownMadeTable
ownMadeTable = pd.DataFrame()
ownMadeTable['restaurant_id'] = tableRestaurants['restaurant_id']
ownMadeTable['ville'] = tableRestaurants['ville']
ownMadeTable['Qaulite'] = tableRestaurants['moyenne_etoiles']

# 1. Filtrer les avis avec des étoiles > 4
avis_filtrés = tableAvis[tableAvis['etoiles'] > 4]

# 2. Compter le nombre d'avis positifs par restaurant_id
avis_count = avis_filtrés.groupby('restaurant_id')['etoiles'].count()

# Ajouter une colonne pour les avis positifs dans ownMadeTable
ownMadeTable['count_avis_positive'] = ownMadeTable['restaurant_id'].map(avis_count).fillna(0)

# 3. Comptage du nombre de fois qu'un **nom de restaurant** apparaît dans tableRestaurants
restaurant_name_counts = tableRestaurants['nom'].value_counts()

# 4. Ajouter cette information dans ownMadeTable en associant le restaurant_id à son nom
# On crée une nouvelle colonne dans ownMadeTable pour y insérer le count des noms
ownMadeTable['count_nom_restaurant'] = ownMadeTable['restaurant_id'].map(
    lambda x: restaurant_name_counts[tableRestaurants.loc[tableRestaurants['restaurant_id'] == x, 'nom'].values[0]]
).fillna(0)

# Affichage du DataFrame final
print(ownMadeTable)
