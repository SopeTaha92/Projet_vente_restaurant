


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
                'total_amount' : 'sum',
                'discount' : 'mean',
                'rating' : 'mean'
            }
        )
        .round(2)
        .sort_values(by=('total_amount'), ascending=False)
        .reset_index()
    )



    logger.info("Analyse par Restaurant éffectué avec succée")
    return df_restaurant


"""





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



"""