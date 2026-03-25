


from loguru import logger

from config import LOGS_FILE, BRUTE_DATA_FILE, MAX_RETRIES, DELAY, CLEAN_DATA_FILE, EXCEL_FILE


from src import logger_file, extracting_data, cleaning_data, add_features, reporting_excel
from src import analysis_by_restaurant, analysis_by_plat, analysis_by_category



logger_file(LOGS_FILE)
logger.info('Lancement du scripte de traitement des données')
brute_data = extracting_data(BRUTE_DATA_FILE, MAX_RETRIES, DELAY)
print(brute_data)
clean_data = cleaning_data(brute_data, CLEAN_DATA_FILE)
complete_data = add_features(clean_data)
analyse_restaurant = analysis_by_restaurant(complete_data)
analyse_plats = analysis_by_plat(complete_data)
analyse_categorie = analysis_by_category(complete_data)

print(complete_data)


Onglets = {
    "Données Brutes" : brute_data,
    "Données aux Complets" : complete_data,
    "Données Par Restaurant" : analyse_restaurant,
    "Données Par Plats" : analyse_plats,
    "Données Par Catégories" : analyse_categorie
}


reporting_excel(EXCEL_FILE, Onglets) 







