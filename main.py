


from loguru import logger

from config import LOGS_FILE, BRUTE_DATA_FILE, CLEAN_DATA_FILE


from src import logger_file, extracting_data



logger_file(LOGS_FILE)
logger.info('Lancement du scripte de traitement des données')
brute_data = extracting_data(BRUTE_DATA_FILE)
print(brute_data)















