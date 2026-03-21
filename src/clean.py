"""




import pandas as pd
import numpy as np
import os
from pathlib import Path
from datetime import datetime


today = datetime.now().strftime("%d-%m-%Y_%H-%M")
dir_path = Path(__file__).parent
os.makedirs(dir_path, exist_ok=True)
file  = dir_path /f"exo_avance_vente_restaurant_{today}.xlsx"

data_restaurant = {
    'order_id': ['REST-001', 'REST-002', 'REST-003', 'REST-004', 'REST-005', 'REST-006', 'REST-007', 'REST-008', 'REST-009', 'REST-010', 'REST-011', 'REST-012'],
    'restaurant': ['paris_central', 'LYON_SUD', 'marseille_vieux_port', 'LILLE_CENTRE', 'TOULOUSE_CAPITOLE', 'BORDEAUX_QUAIS', 'NICE_PROMENADE', 'STRASBOURG_GRANDE_ILE', 'MONTPELLIER_ECUSSON', 'RENNES_CENTRE', 'paris_central', 'LYON_SUD'],
    'customer_name': ['alice martin', 'BOB DUPONT', 'charlie legrand', 'diana roy', 'evelyn tremblay', 'frank klein', 'grace leroy', 'henry gauthier', 'ivana petrov', 'jack wilson', 'sophie bernard', 'lucas moreau'],
    'order_date': ['15/03/2024', '2024-03-16', '17/03/2024', '2024-03-18', '19/03/2024', '2024-03-20', '21/03/2024', '2024-03-22', '23/03/2024', '2024-03-24', '25/03/2024', '2024-03-26'],
    'order_time': ['19:30', '20:15', '21:00', '19:45', '20:30', '21:15', '19:00', '20:45', '21:30', '19:15', '20:00', '21:45'],
    'menu_item': ['Pizza Margherita', 'BURGER CLASSIC', 'salade cesar', 'PASTA CARBONARA', 'Steak frites', 'POISSON DU JOUR', 'PLAT VEGETARIEN', 'ASSIETTE FROMAGES', 'DESSERT MAISON', 'CAFE GOURMAND', 'Pizza Margherita', 'BURGER CLASSIC'],
    'category': ['PIZZA', 'BURGER', 'SALAD', 'PASTA', 'MAIN COURSE', 'FISH', 'VEGETARIAN', 'CHEESE', 'DESSERT', 'DESSERT', 'PIZZA', 'BURGER'],
    'quantity': ['1', '2', '1', '1', '1', '1', '2', '1', '3', '2', '1', '2'],
    'unit_price': ['12.50€', '15.00', '9.80€', '14.20€', '18.50', '22.00€', '16.80', '12.00€', '6.50€', '8.00', '12.50€', '15.00'],
    'discount': ['0%', '10%', '5%', '0%', '15%', '0%', '10%', '5%', '20%', '0%', '0%', '10%'],
    'payment_method': ['CARD', 'CASH', 'CARD', 'CARD', 'CASH', 'CARD', 'CARD', 'CASH', 'CARD', 'CARD', 'CASH', 'CARD'],
    'rating': ['5', '4', '4', '5', '3', '5', '4', '4', '5', '4', '5', '4']
}

df_resto = pd.DataFrame(data_restaurant)
print("🍽️ DONNÉES RESTAURANT BRUTES :")
print(df_resto)

df_resto = df_resto.drop_duplicates()
df_resto['restaurant'] = (
    df_resto['restaurant']
    .str.replace("_", " ", regex=False)
    .str.title()
)

df_resto['order_date'] = pd.to_datetime(
    df_resto['order_date'],
    format='mixed',# ← "Devine le format pour chaque valeur" avec python 3.11+
    dayfirst=True,# ← "Priorité jour/mois pour l'Europe"
    errors='coerce' # ← "Ne plante pas si échec met Nat
).dt.strftime("%d-%m-%Y")#Pour changer le format d'affichage de la date par defaut sur python yyyy-mm-dd 
df_resto['order_time'] = pd.to_datetime(df_resto['order_time'], format='%H:%M').dt.time

df_resto['customer_name'] = df_resto['customer_name'].str.title()
df_resto['menu_item'] = df_resto['menu_item'].str.title()
df_resto['category'] = df_resto['category'].str.title()
df_resto['quantity'] = df_resto['quantity'].fillna(1).astype(int)
df_resto['unit_price'] = (
    df_resto['unit_price']
    .str.replace("€", "", regex=False)
    .str.replace(" ", "", regex=False)
    .replace("", "0", regex=False)
    .astype(float)
    .round(2)
)
df_resto['rating'] = df_resto['rating'].astype(int)

df_resto['discount'] = (
    df_resto['discount']
    .str.replace("%", "", regex=False)
    .str.replace(" ", "", regex=False)
    .replace("", "0", regex=False)
    .astype(int)
) 
df_resto['discount'] = round(df_resto['discount'] /100, 2)

df_nettoye = pd.DataFrame(df_resto)

df_nettoye['total_amount'] = round(df_nettoye['unit_price'] * df_nettoye['quantity'], 2).astype(float)
df_nettoye['service_type'] = df_nettoye['order_time'].apply(lambda x : 'Soir' if x.hour >= 19 else 'Dejeuner')
df_nettoye['order_datetime'] = pd.to_datetime(
    df_nettoye['order_date'].astype(str) +' ' +  df_nettoye['order_time'].astype(str),
    errors='coerce'
)

df_nettoye['marge'] = round(df_nettoye['unit_price'] * 0.40, 2).astype(float)

df_nettoye = df_nettoye.drop(['order_date', 'order_time'], axis=1)


df_restaurant = (
    df_nettoye
    .groupby('restaurant')
    .agg(
        {
            'total_amount' : 'sum',
            'quantity' : 'sum',
            'rating' : 'mean'
        }
    )
    .round(2)
    .sort_values(by=('total_amount'), ascending=False)
    .reset_index()
)



df_plats = (
    df_resto
    .groupby('menu_item')
    .agg(
        {
            'quantity' : 'sum',
            'unit_price' : 'first'
        }
    )
    .sort_values(by='quantity', ascending=False)
    .reset_index() 
    )



df_plats['total_amount'] = round((df_plats['unit_price'] * df_plats['quantity']), 2)



df_category = (
    df_resto.groupby('category')
    .agg(
        {
           'quantity' : 'sum',
           'unit_price' : 'mean'
        }
    )
    .reset_index() 
)


df_category['Impact_CA_%'] = round(((df_category['quantity'] * df_category['unit_price']) / df_plats['total_amount'].sum()) * 100, 2)





print()
print(f"🧹 NETTOYAGE COMPLEXE\n{df_nettoye}")

df_restaurant['rating'] = df_restaurant['rating'].astype(str) + '/5'
df_restaurant['total_amount'] = df_restaurant['total_amount'].astype(str) + ' €'

print()
print(f"🧹 Donnée par Restaurant\n{df_restaurant}")

df_plats['unit_price'] = df_plats['unit_price'].astype(str) + ' €'
df_plats['total_amount'] = df_plats['total_amount'].astype(str) + ' €'

print()
print(f"🧹 Donnée par Plats\n{df_plats}")

df_category['unit_price'] = df_category['unit_price'].astype(str) + ' €'
df_category['Impact_CA_%'] = df_category['Impact_CA_%'].astype(str) + ' %'

print()
print(f"🧹 Donnée par Catégories\n{df_category}")

"""