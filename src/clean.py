


import pandas as pd
from loguru import logger
from config import CLEAN_DATA_FILE


def cleaning_data(df_brute : pd.DataFrame, file : str = CLEAN_DATA_FILE) -> pd.DataFrame:
    """Cette fonction se charge du néttoyage des données brutes"""
    logger.info('Début du néttoyage des données brutes')
    df_resto = df_brute.copy()
    logger.info('Copie des données brutes éffectué')

    df_resto = df_resto.drop_duplicates(keep='first')
    logger.info('Suppréssion des potentiels doublons')

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
    ).dt.date#.dt.strftime("%d-%m-%Y")#Pour changer le format d'affichage de la date par defaut sur python yyyy-mm-dd 

    df_resto['order_time'] = pd.to_datetime(df_resto['order_time'], errors='coerce').dt.time

    df_resto['customer_name'] = df_resto['customer_name'].str.title().fillna('Inconnue')

    df_resto['menu_item'] = df_resto['menu_item'].str.title().fillna('Inconnue')

    df_resto['category'] = df_resto['category'].str.title().fillna('Inconnue')

    df_resto['quantity'] = df_resto['quantity'].fillna(1).astype(int)

    df_resto['unit_price'] = (
        df_resto['unit_price']
        .str.replace("€", "", regex=False)
        .str.replace(" ", "", regex=False)
        .replace("", "0", regex=False)
        .astype(float)
        .round(2)
    )

    df_resto['rating'] = df_resto['rating'].astype(int).fillna(0)

    df_resto['discount'] = (
        df_resto['discount']
        .str.replace("%", "", regex=False)
        .str.replace(" ", "", regex=False)
        .replace("", "0", regex=False)
        .astype(int)
    ) 


    logger.info('Néttoyage des données brutes éffectue avec succée')

    df_resto.to_csv(file, index=False)
    logger.info(f'Données néttoyés sont sauvegardés dans {file.name}')
    return df_resto


"""


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