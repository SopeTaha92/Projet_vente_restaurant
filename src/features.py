


import pandas as pd
from loguru import logger


def add_features(df_nettoye : pd.DataFrame) -> pd.DataFrame:
    """Cette fonction se charge d'ajouter des nouvelles colonnes à travers les divers opérations qui seront éffectués"""
    logger.info('Début des features')

    df_nettoye['total_price'] = round(df_nettoye['unit_price'] * df_nettoye['quantity'], 2).astype(float)

    df_nettoye['discount_amount'] = round((df_nettoye['total_price'] * df_nettoye['discount']) / 100, 2).astype(float)

    df_nettoye['total_amount'] = round((df_nettoye['total_price'] - df_nettoye['discount_amount']), 2).astype(float)


    df_nettoye['service_type'] = df_nettoye['order_time'].apply(lambda x : 'Soir' if x.hour >= 19 else 'Dejeuner')
    """df_nettoye['order_datetime'] = pd.to_datetime(
        df_nettoye['order_date'].astype(str) +' ' +  df_nettoye['order_time'].astype(str),
        errors='coerce'
    )"""

    #df_nettoye = df_nettoye.drop(['order_date', 'order_time'], axis=1)
    logger.info('Ajout des nouvelles colonnes éffectue avec succée')
    return df_nettoye