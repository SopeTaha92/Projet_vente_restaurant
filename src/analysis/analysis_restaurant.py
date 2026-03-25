


import pandas as pd
from loguru import logger


def analysis_by_restaurant(df_nettoye : pd.DataFrame):
    """Cette fonction s'occupe des analyse par restaurant"""
    logger.info("Début des analyses par Restaurant")
    df_restaurant = (
        df_nettoye
        .groupby('restaurant')
        .agg(
            {
                'menu_item' : 'count',
                'quantity' : 'sum',
                'total_price' : 'sum',
                'discount' : 'mean',
                'total_amount' : 'sum',
                'rating' : 'mean'
            }
        )
        .round(2)
        .sort_values(by=('total_amount'), ascending=False)
        .reset_index()
    )



    logger.info("Analyse par Restaurant éffectué avec succée")
    return df_restaurant


