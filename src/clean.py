


import pandas as pd
from loguru import logger
from config import CLEAN_DATA_FILE


def cleaning_data(df_brute : pd.DataFrame, file : str = CLEAN_DATA_FILE) -> pd.DataFrame:
    """Cette fonction se charge du néttoyage des données brutes"""
    logger.info('Début du néttoyage des données brutes')
    logger.info(f"Lignes brutes {len(df_brute)}")
    df_resto = df_brute.copy()
    logger.info('Copie des données brutes éffectué')

    df_resto = df_resto.drop_duplicates(keep='first')
    logger.info(f'Suppréssion des doublons soit : {len(df_brute) - len(df_resto)} lignes')

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

    df_resto['order_time'] = pd.to_datetime(df_resto['order_time'], format='mixed', errors='coerce').dt.time

    df_resto['customer_name'] = df_resto['customer_name'].str.title().fillna('Inconnue')

    df_resto['menu_item'] = df_resto['menu_item'].str.title().fillna('Inconnue')

    df_resto['category'] = df_resto['category'].str.title().fillna('Inconnue')

    df_resto['quantity'] = pd.to_numeric(df_resto['quantity'], errors='coerce', downcast='integer').fillna(1).astype(int) 

    df_resto['unit_price'] = (
        pd.to_numeric(
            df_resto['unit_price']
            .astype(str)
            .str.extract(r"(\d+[\,.]?\d*)")[0]
            .str.replace(",", ".", regex=False),
            errors='coerce'
            ).fillna(0).round(2)
    )

    df_resto['rating'] = pd.to_numeric(df_resto['rating'], errors='coerce').fillna(0).astype(int)

    df_resto['discount'] = (
        pd.to_numeric(
            df_resto['discount']
            .astype(str)
            .str.extract(r"(\d+)")[0],
            errors='coerce',
            downcast='integer'
        ).fillna(0).astype(int)
    ) 

    df_resto['payment_method'] = df_resto['payment_method'].str.upper().fillna('Inconnue')


    logger.info('Néttoyage des données brutes éffectue avec succée')
    logger.info(f"Lignes néttoyées {len(df_resto)}")

    df_resto.head(10).to_csv(file, index=False)
    logger.info(f"Échantillon de {len(df_resto.head(10))} lignes sauvegardé dans {file}")
    logger.info(f"Données nettoyées prêtes pour le pipeline : {len(df_resto)} lignes")
    return df_resto

