


from pathlib import Path
from datetime import datetime


TODAY = datetime.now().strftime('%d-%m-Y_%H-%M')
MAX_RETRIES = 3
DELAY = 1


DIR_LOGS = Path('Logs')
DIR_LOGS.mkdir(parents=True, exist_ok=True)
LOGS_FILE = DIR_LOGS / f'log_vente_restaurant_{TODAY}.log'

BRUTE_DATA_FILE = Path('data/raw/vente_restaurant.csv')

DIR_CLEAN_DATA = Path('data/processed')
DIR_CLEAN_DATA.mkdir(parents=True, exist_ok=True)
CLEAN_DATA_FILE = DIR_CLEAN_DATA / 'clean_vente_restaurant.csv'




