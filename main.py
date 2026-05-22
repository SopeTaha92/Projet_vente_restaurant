


import time
from loguru import logger



from src import logger_file, extracting_data, cleaning_data, add_features, injection_complet_data__to_sql, reporting_excel, send_mail
from src import analysis_by_restaurant, analysis_by_plat, analysis_by_category

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
    details = f"""
    • Lignes brutes : {len(brute_data)}
    • Lignes traitées : {len(clean_data)}
    • Lignes injectées : {len(complete_data)}
    • Rapport Excel : généré dans Output/
    • Dashboard Power BI connecté à la DB : à actualiser
    • Durée du Pipeline : {duration:.2f} secondes
            """
    send_mail(status=True, details=details)
except Exception as e:
    logger.exception(f"Echec du pipeline {e}")
    details = f"Type d'erreur : {type(e).__name__}\nMessage : {str(e)}"
    send_mail(status=False, details=details)
    raise







