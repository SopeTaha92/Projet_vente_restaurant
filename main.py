


import time
from loguru import logger



from src import logger_file, extracting_data, cleaning_data, add_features, injection_complet_data__to_sql, reporting_excel
from src import analysis_by_restaurant, analysis_by_plat, analysis_by_category
#from config import COMPLATE_DATA_FILE

start_time = time.time()

try:
    logger_file()
    logger.info('Lancement du scripte de traitement des données')
    brute_data = extracting_data()
    clean_data = cleaning_data(brute_data)
    complete_data = add_features(clean_data)
    injection_complet_data__to_sql(complete_data)
    analyse_restaurant = analysis_by_restaurant(complete_data)
    analyse_plats = analysis_by_plat(complete_data)
    analyse_categorie = analysis_by_category(complete_data)


    onglets = {
        "Données Brutes" : brute_data,
        "Données aux Complets" : complete_data,
        "Données Par Restaurant" : analyse_restaurant,
        "Données Par Plats" : analyse_plats,
        "Données Par Catégories" : analyse_categorie 
    }


    reporting_excel(onglets)
    duration = time.time() - start_time
    logger.info(f"Pipeline exécuté en {duration:.2f} secondes")
except Exception as e:
    logger.exception(f"Echec du pipeline {e}")
    raise







