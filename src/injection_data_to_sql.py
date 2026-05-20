


import pandas as pd
from loguru import logger
import psycopg2
from psycopg2.extras import execute_batch
from config import DB_CONFIG, TABLE_CLEAN


def injection_complet_data__to_sql(df_complet : pd.DataFrame, db_config : dict = DB_CONFIG, table : str = TABLE_CLEAN) -> None:
    """
    Injecte le DataFrame dans PostgreSQL avec execute_batch.
    
    Args:
        df_complet: DataFrame à injecter
        db_config: Configuration de connexion (utilise DB_CONFIG par défaut)
    
    Returns:
        None : juste injecté les données 
    
    Raises:
        ValueError: Si le DataFrame est vide
    """

    logger.info("Début de l'injection des données")

    if df_complet.empty:
        logger.warning("Le DataFrame est vide. Rien à injecter.")
        return
    
    logger.info(f"Début de l'injection - {len(df_complet)} lignes à traiter")

    colonnes = list(df_complet.columns)
    placeholders = ', '.join(['%s'] * len(colonnes))

    query = f"insert into {table} ({', '.join(colonnes)}) values ({placeholders})"

    data_to_insert = [tuple(x) for x in df_complet[colonnes].values]

    try:
        with psycopg2.connect(**db_config) as conn:
            with conn.cursor() as cur:
                cur.execute(f"TRUNCATE TABLE {table} RESTART IDENTITY;")
                logger.info(f"Table {table} vidée avant injection")
                logger.info(f"Injection de {len(data_to_insert)} lignes")
                execute_batch(cur, query, data_to_insert, page_size=1000)
                logger.info("Données injectées avec succès ! ✨")
    except Exception as e:
        logger.error(f"Erreur critique lors de l'injection des données : {e}")
        raise




"""(    query = "
        INSERT INTO ventes (
                    id, order_id, restaurant, customer_name, order_date, order_time, 
                    menu_item, category, quantity, unit_price, discount, 
                    payment_method, rating, total_price, service_type
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                "

    query = f"
                insert into {table} (
                    id, order_id, restaurant, customer_name, order_date, order_time, 
                    menu_item, category, quantity, unit_price, discount, 
                    payment_method, rating, total_price, service_type
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            ") 
    """

"""    missing_cols = set(colonnes) - set(df_complet.columns)
    if missing_cols:
        raise ValueError(f"Colonnes manquantes : {missing_cols}")
        """