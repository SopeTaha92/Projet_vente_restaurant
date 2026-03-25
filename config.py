


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

DIR_EXCEL = Path('Output')
DIR_EXCEL.mkdir(parents=True, exist_ok=True)
EXCEL_FILE = DIR_EXCEL / f"vente_restaurant_{TODAY}.xlsx"


COULEURS_EXCEL= {
    'vert': '#C6EFCE',
    'rouge': '#FFC7CE',
    'orange': '#FFEB9C',
    'header': '#4472C4',  # Bleu professionnel pour RH
    'expert': '#9BC2E6',   # Bleu clair
    'senior': '#A9D08E',   # Vert
    'junior': '#FFD966'    # Jaune
}




