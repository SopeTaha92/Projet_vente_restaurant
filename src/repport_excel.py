


import pandas as pd
from typing import Dict
from loguru import logger
import config
from config import EXCEL_FILE

def reporting_excel(onglets : Dict[str, pd.DataFrame], file : str = EXCEL_FILE):
    """Cette fonction se charge de la génération du fichier Excel avec ses Multiples feuilles"""
    logger.info(f"Début de la génération du fichier Excel {file.name}")
    with pd.ExcelWriter(file, engine='xlsxwriter') as writer:
        logger.info("Ouverture du contexte manager")
        workbook = writer.book

        header = config.COULEURS_EXCEL['header']
        rouge = config.COULEURS_EXCEL['rouge']
        orange = config.COULEURS_EXCEL['orange']
        vert = config.COULEURS_EXCEL['vert']

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
        discount_format = workbook.add_format({**base, 'num_format' : '0" %"'})
        money_format = workbook.add_format({**base, 'num_format' : '#,##0.00 €'})
        rating_format = workbook.add_format({**base, 'num_format' : '0" / 5"'})

        red_format = workbook.add_format({**base, 'bg_color' : rouge})
        green_format = workbook.add_format({**base, 'bg_color' : vert})
        orange_format = workbook.add_format({**base, 'bg_color' : orange})

        COLONNE_FORMATER_COMPLET = {
            'discount' : {
                'colonne' : 'discount',
                'seuil_key' : 'discount'
            },

            'discount_amount' : {
                'colonne' : 'discount_amount',
                'seuil_key' : 'discount_amount'
            },

            'total_amount' : {
                'colonne' : 'total_amount',
                'seuil_key' : 'total_amount'
            }
        }

        COLONNE_FORMATER_ANALYSIS = {

            'discount' : {
                'colonne' : 'discount',
                'seuil_key' : 'discount'
            },

            'discount_amount' : {
                'colonne' : 'discount_amount',
                'seuil_key' : 'discount_amount'
            },

            'total_amount_pl' : {
                'colonne' : 'total_amount',
                'seuil_key' : 'total_amount_pl'
            }
        }

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
                    discount_column = ['discount', 'Impact_CA_%']
                    money_column = ['unit_price', 'discount_amount', 'total_price', 'total_amount']
                    if column in discount_column:
                        worksheet.set_column(i, i, column_width, discount_format)
                    elif column in money_column:
                        worksheet.set_column(i, i, column_width, money_format)
                    elif column == 'rating':
                        worksheet.set_column(i, i, column_width, rating_format)
                    else:
                        worksheet.set_column(i, i, column_width, base_format)
                logger.info(f"Ajustement automatique de la taille des cellules et de l'ajout des divers foramatage pour la feuille {name}")
                
                if name == 'Données aux Complets':
                    logger.info(f"Application de la mise en forme conditionnelle sur la feuille {name}")

                    for col_form in COLONNE_FORMATER_COMPLET.values():
                        colone_name = col_form['colonne']
                        seuil_key = col_form['seuil_key']
                        if colone_name in data.columns:
                            discount_column = data.columns.get_loc(colone_name)
                            seuil = config.EXCEL_FORMATTING[seuil_key]

                            worksheet.conditional_format(1, discount_column, len(data), discount_column, {
                                'type' : 'cell',
                                'criteria' : '<=',
                                'value' : seuil['red_value'],
                                'format' : red_format
                            })

                            worksheet.conditional_format(1, discount_column, len(data), discount_column, {
                                'type' : 'cell',
                                'criteria' : '>',
                                'value' : seuil['green_value'],
                                'format' : green_format
                            })

                            worksheet.conditional_format(1, discount_column, len(data), discount_column, {
                                'type' : 'cell',
                                'criteria' : 'between',
                                'minimum' : seuil['min_orange'],
                                'maximum' : seuil['max_orange'],
                                'format' : orange_format
                            })

                analysis_column = ['Données Par Restaurant', 'Données Par Plats', 'Données Par Catégories']
                if name in analysis_column:
                    logger.info(f"Application de la mise en forme conditionnelle sur la feuille {name}")

                    for col_form in COLONNE_FORMATER_ANALYSIS.values():
                        colone_name = col_form['colonne']
                        seuil_key = col_form['seuil_key']
                        if colone_name in data.columns:
                            discount_column = data.columns.get_loc(colone_name)
                            seuil = config.EXCEL_FORMATTING[seuil_key]

                            worksheet.conditional_format(1, discount_column, len(data), discount_column, {
                                'type' : 'cell',
                                'criteria' : '<=',
                                'value' : seuil['red_value'],
                                'format' : red_format
                            })

                            worksheet.conditional_format(1, discount_column, len(data), discount_column, {
                                'type' : 'cell',
                                'criteria' : '>',
                                'value' : seuil['green_value'],
                                'format' : green_format
                            })

                            worksheet.conditional_format(1, discount_column, len(data), discount_column, {
                                'type' : 'cell',
                                'criteria' : 'between',
                                'minimum' : seuil['min_orange'],
                                'maximum' : seuil['max_orange'],
                                'format' : orange_format
                            })
                            