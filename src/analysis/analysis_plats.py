


import pandas as pd
from loguru import logger


def analysis_by_plat(df_nettoye : pd.DataFrame):
    """Cette fonction s'occupe des analyse par Plat"""
    logger.info("Début des analyses par Plat")

    df_plats = (
        df_nettoye
        .groupby('menu_item')
        .agg(
            {
                'unit_price' : 'first',
                'quantity' : 'sum',
                'discount' : 'mean',
                'rating' : 'mean'
                
            }
        )
        .sort_values(by='quantity', ascending=False)
        .reset_index() 
        )

    df_plats['total_amount'] = round((df_plats['unit_price'] * df_plats['quantity']), 2).astype(float)

    logger.info("Analyse par Plat éffectué avec succée")
    return df_plats


