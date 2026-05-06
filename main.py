


from loguru import logger



from src import logger_file, extracting_data, cleaning_data, add_features, reporting_excel
from src import analysis_by_restaurant, analysis_by_plat, analysis_by_category


try:
    logger_file()
    logger.info('Lancement du scripte de traitement des données')
    brute_data = extracting_data()
    clean_data = cleaning_data(brute_data)
    complete_data = add_features(clean_data)
    analyse_restaurant = analysis_by_restaurant(complete_data)
    analyse_plats = analysis_by_plat(complete_data)
    analyse_categorie = analysis_by_category(complete_data)


    Onglets = {
        "Données Brutes" : brute_data,
        "Données aux Complets" : complete_data,
        "Données Par Restaurant" : analyse_restaurant,
        "Données Par Plats" : analyse_plats,
        "Données Par Catégories" : analyse_categorie 
    }


    reporting_excel(Onglets) 
except Exception as e:
    logger.exception(f"Echec du pipeline {e}")
    raise







