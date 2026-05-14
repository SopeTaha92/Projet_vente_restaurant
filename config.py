


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

TODAY = datetime.now().strftime('%d-%m-%Y_%H-%M')
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


EXCLUDED_SHEETS = ['Données Brutes']

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

    'Données aux Complets' : {
        'total_amount' : {'red_value': 10, 'min_orange': 10, 'max_orange': 20, 'green_value': 20},
        'discount' : {'red_value': 5, 'min_orange': 6, 'max_orange': 15, 'green_value': 15},
        'discount_amount' : {'red_value': 0.5, 'min_orange': 0.5, 'max_orange': 2.5, 'green_value': 2.5}
    },

    'Données Par Restaurant' : {
        'total_amount' : {'red_value': 15, 'min_orange': 15, 'max_orange': 40, 'green_value': 40},
        'discount' : {'red_value': 5, 'min_orange': 6, 'max_orange': 15, 'green_value': 15}
    },

    'Données Par Plats' : {
        'total_amount' : {'red_value': 12, 'min_orange': 12, 'max_orange': 30, 'green_value': 30},
        'discount' : {'red_value': 5, 'min_orange': 6, 'max_orange': 15, 'green_value': 15}
    },

    'Données Par Catégories' : {
        'total_amount' : {'red_value': 15, 'min_orange': 15, 'max_orange': 40, 'green_value': 40},
        'Impact_CA_%' : {'red_value': 5, 'min_orange': 5, 'max_orange': 15, 'green_value': 15},
        'discount' : {'red_value': 5, 'min_orange': 6, 'max_orange': 15, 'green_value': 15}
    }
}

OPTIONS_DATA_LABELS = {'value', 'category', 'percentage', 'num_format', 'position'}
OPTIONS_MARKER_LINE = {'type', 'size'}

EXCEL_CHARTS = {
    'Données Par Restaurant': {
        'type': 'column',
        'title': 'Performance par Restaurant',
        'x_axis_col': 'restaurant',
        'series': [
            {
                'name': 'Total Amount',
                'y_axis_col': 'total_amount',
                'fill': '#4472C4',
                'border' : {'color' : "#E1E4EB", 'width' : 1.5},
                'data_labels' : {
                    'value' : True,
                    'num_format' : '#,##0.00 €',
                    'position' : 'outside_end',
                    'font' : {'bold' : True}
                }
            },
            {
                'name': 'Rating',
                'y_axis_col': 'rating',
                'type': 'line',
                'y2_axis': True,
                'line_color': 'red',
                'data_labels' : {
                    'value' : True,
                    'num_format' : '0',
                    'position' : 'above',
                    'font' : {'bold' : True}
                },
                'marker': {
                    'type': 'circle', 
                    'size': 5, 
                    'fill': {'color': 'white'}, 
                    'border': {'color': 'red'}
                    }
            }
        ]
    },

    'Données Par Plats' : {
        'type' : 'pie',
        'title' : 'Répartion par Plats',
        'x_axis_col' : 'menu_item',
        'series' : [
            {
                'name' : 'Revenue par Plat',
                'y_axis_col' : 'total_amount',
                'data_labels' : {
                    'percentage' : True,
                    'category' : True,
                    'position' : 'outside_end'
                }
            }
        ]
    },

    'Données Par Catégories': {
        'type': 'column',
        'title': 'Performance par Catégorie',
        'x_axis_col': 'category',
        'series': [
            {
                'name': 'Total Amount',
                'y_axis_col': 'total_amount',
                'fill': '#4472C4',
                'border' : {'color' : "#E1E4EB", 'width' : 1.5},
                'data_labels' : {
                    'value' : True,
                    'num_format' : '#,##0.00 €',
                    'position' : 'outside_end',
                    'font' : {'bold' : True}
                }
            },
            {
                'name': 'Impacte sur le CA',
                'y_axis_col': 'Impact_CA_%',
                'type': 'line',
                'y2_axis': True,
                'line_color': 'red',
                'data_labels' : {
                    'value' : True,
                    'num_format' : '0 %',
                    'position' : 'above',
                    'font' : {'bold' : True}
                },
                'marker': {
                    'type': 'circle', 
                    'size': 5, 
                    'fill': {'color': 'white'}, 
                    'border': {'color': 'red'}
                    }
            }
        ]
    }
}
