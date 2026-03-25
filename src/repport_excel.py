


import pandas as pd
from typing import Dict
from loguru import logger
import config

def reporting_excel(file : str, onglets : Dict[str, pd.DataFrame]):
    """Cette fonction se charge de la génération du fichier Excel avec ses Multiples feuilles"""
    logger.info(f"Début de la génération du fichier Excel {file.name}")
    with pd.ExcelWriter(file, engine='xlsxwriter') as writer:
        logger.info("Ouverture du contexte manager")
        workbook = writer.book
        header = config.COULEURS_EXCEL['header']
        base = {
            'align' : 'center',
            'valign' : 'center',
            'border' : 1
        }

        base_format = workbook.add_format(base)
        header_format = workbook.add_format(
            {
                **base,
                'bold' : True,
                'italic' : True,
                'bg_color' : header,
                'font_color' : 'white'
            }
        )

        for name, data in onglets.items():
            data.to_excel(writer, sheet_name=name, index=False)
            logger.info(f'Créationde la feuille {name}')
            worksheet = writer.sheets[name]

            colonne_traite = ['Données aux Complets', 'Données Par Restaurant', 'Données Par Plats', 'Données Par Catégories']
            if name in colonne_traite:
                worksheet.freeze_panes(1, 0)
                logger.info(f'Fixation des entêtes pour la feuille {name}')

                worksheet.autofilter(0, 0, len(data), len(data.columns) - 1)
                logger.info(f'Application des auto_filtres sur les entêtes de la feuille {name}')

                for column_numb, value in enumerate(data.columns):
                    worksheet.write(0, column_numb, value, header_format)
                logger.info(f'Application des couleurs sur les entêtes de la feuille {name}')

                for i, column in enumerate(data.columns):
                    column_width = max(data[column].astype(str).str.len().max() , len(column)) + 3
                    worksheet.set_column(i, i, column_width, base_format)
                logger.info(f'Ajustement automatique de la taille des cellules pour la feuille {name}')