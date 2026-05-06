


from pathlib import Path
from datetime import datetime
from dotenv import dotenv_values


env = dotenv_values(".env")
DB_CONFIG = {
    'host' : env['DB_HOST'],
    'port' : int(env['DB_PORT']),
    'dbname' : env['DB_NAME'],
    'user' : env['DB_USER'],
    'password' : env['DB_PASSWORD']
}

TABLE = env['DB_TABLE']

TODAY = datetime.now().strftime('%d-%m-Y_%H-%M')
MAX_RETRIES = 3
DELAY = 1


DIR_LOGS = Path('Logs')
DIR_LOGS.mkdir(parents=True, exist_ok=True)
LOGS_FILE = DIR_LOGS / f'log_vente_restaurant_{TODAY}.log'

DIR_BRUTE_DATA_FILE = Path('data/raw')
DIR_BRUTE_DATA_FILE.mkdir(parents=True, exist_ok=True)
BRUTE_DATA_FILE = DIR_BRUTE_DATA_FILE / 'vente_restaurant.csv'

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

EXCEL_FORMATTING = {

    'discount' : {
        'red_value' : 5,
        'min_orange' : 6,
        'max_orange' : 15,
        'green_value' : 15
    },

    'discount_amount' : {
        'red_value' : 0.5,
        'min_orange' : 0.5,
        'max_orange' : 2.5,
        'green_value' : 2.5
    },

    'total_amount' : {
        'red_value' : 15,
        'min_orange' : 15,
        'max_orange' : 25,
        'green_value' : 25
    },

    'total_amount_pl' : {
        'red_value' : 15,
        'min_orange' : 15,
        'max_orange' : 25,
        'green_value' : 25
    }
}




