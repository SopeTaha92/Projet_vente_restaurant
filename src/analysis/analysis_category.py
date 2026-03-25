


import pandas as pd
from loguru import logger


def analysis_by_category(df_nettoye : pd.DataFrame):
    """Cette fonction s'occupe des analyse par Catégorie"""
    logger.info("Début des analyses par Catégorie")


    df_category = (
        
        df_nettoye.groupby('category')
         
        .agg(
            {
            #'unit_price' : 'mean',
            'quantity' : 'sum',
            'total_price' : 'sum',
            'discount' : 'mean',
            'total_amount' : 'sum',
            'rating' : 'mean'
            
            }
        )
        .reset_index() 
    )

    #df_category['unit_price_mean'] = df_nettoye['unit_price'].mean()
    
    df_category['Impact_CA_%'] = round((df_category['total_price'] / df_nettoye['total_amount'].sum()) * 100, 2).astype(float)

    logger.info("Analyse par Catégorie éffectué avec succée")
    return df_category

