


import sys
import time
import pandas as pd 
from loguru import logger


def extracting_data(file : str, max_retries : int, delay : int):
    """Cette fonction se charge de l'extraction des données brutes depuis le fichier source (CSV) """
    logger.info("Début de l'extraction des données brutes")
    for retry in range(max_retries):
        try:
            brute_data = pd.read_csv(file)
            logger.info('Extraction des données brutes éffectués avec succée')
            return brute_data
        except FileNotFoundError as e:
            logger.error(f"Fichier des données brutes introuvable : {e}")
            if retry < max_retries - 1:
                logger.error(f'Echec de la tentative {retry} / {max_retries}')
                logger.info(f'Nouvelle tentative dans {delay} secondes')
                time.sleep(delay)
                delay *= 2
    logger.critical(f"Echec de l'extraction des données brutes après {max_retries} tentatives")
    sys.exit("Arret du programme :  impossible de chargé la source de donnée")
            