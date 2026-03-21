


from loguru import logger

from config import LOGS_FILE, BRUTE_DATA_FILE, MAX_RETRIES, DELAY


from src import logger_file, extracting_data, cleaning_data, add_features



logger_file(LOGS_FILE)
logger.info('Lancement du scripte de traitement des données')
brute_data = extracting_data(BRUTE_DATA_FILE, MAX_RETRIES, DELAY)
print(brute_data)
clean_data = cleaning_data(brute_data)
complete_data = add_features(clean_data)

print(complete_data)















