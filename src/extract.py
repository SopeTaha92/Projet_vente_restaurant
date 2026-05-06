


import sys
import time
import pandas as pd 
import psycopg2
from config import DB_CONFIG, TABLE, MAX_RETRIES, DELAY, BRUTE_DATA_FILE
from loguru import logger


def extracting_data(max_retries : int = MAX_RETRIES, delay : int = DELAY, file : str = BRUTE_DATA_FILE) -> pd.DataFrame:
    """Cette fonction se charge de l'extraction des données brutes depuis la base de donnée"""
    logger.info("Début de l'extraction des données brutes")
    for retry in range(max_retries):
        try:
            with psycopg2.connect(**DB_CONFIG) as conn:
                logger.info('testing connection !')
                query = (f'SELECT * FROM {TABLE};')
                brute_data = pd.read_sql(query, conn)
                logger.info('Extraction des données brutes éffectués avec succée')
                brute_data.to_csv(file)
                return brute_data
        except Exception as e:
            if retry < max_retries - 1:
                logger.error(f'Echec de la tentative {retry+1} / {max_retries}')
                logger.info(f'Nouvelle tentative dans {delay} secondes')
                time.sleep(delay)
                delay *= 2
            else:
                logger.critical(f"Echec total après {max_retries} tentatives : {e}")
    sys.exit("Arret du programme :  impossible de chargé la source de donnée")
            