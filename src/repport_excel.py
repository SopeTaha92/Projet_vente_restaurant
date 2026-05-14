


import pandas as pd
from typing import Dict
from loguru import logger
import config
from config import EXCEL_FILE, EXCLUDED_SHEETS, EXCEL_FORMATTING, EXCEL_CHARTS, OPTIONS_DATA_LABELS, OPTIONS_MARKER_LINE

def reporting_excel(onglets : Dict[str, pd.DataFrame], file : str = EXCEL_FILE, options_labels : str = OPTIONS_DATA_LABELS, options_marker : str = OPTIONS_MARKER_LINE):
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

        for name, data in onglets.items():
            data.to_excel(writer, sheet_name=name, index=False)
            logger.info(f'Créationde la feuille {name}')
            worksheet = writer.sheets[name]

            if name.strip() not in EXCLUDED_SHEETS:
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



            if name in EXCEL_FORMATTING:
                logger.info(f"Application du formatage sur la feuille {name}")

                sheet_formatting_config = EXCEL_FORMATTING[name]

                for col_name, seuil in sheet_formatting_config.items():
                    logger.info(f"Recupération des Clés et Valeurs sur la colonne {col_name} pour la feuille {name}")

                    if col_name in data.columns:

                        col_loc = data.columns.get_loc(col_name)

                        if 'red_value' in seuil:
                                worksheet.conditional_format(1, col_loc, len(data), col_loc, {
                                    'type' : 'cell',
                                    'criteria' : '<=',
                                    'value' : seuil['red_value'],
                                    'format' : red_format
                                })

                        if 'green_value' in seuil:
                            worksheet.conditional_format(1, col_loc, len(data), col_loc, {
                                'type' : 'cell',
                                'criteria' : '>',
                                'value' : seuil['green_value'],
                                'format' : green_format
                            })

                        if 'min_orange' in seuil and 'max_orange' in seuil:
                            worksheet.conditional_format(1, col_loc, len(data), col_loc, {
                                'type' : 'cell',
                                'criteria' : 'between',
                                'minimum' : seuil['min_orange'],
                                'maximum' : seuil['max_orange'],
                                'format' : orange_format
                            })




            if name in EXCEL_CHARTS:
                logger.info(f"Mise en place des graphiques sur la feuille {name}")

                sheet_chart_config = EXCEL_CHARTS[name]
                x_axis_col = data.columns.get_loc(sheet_chart_config['x_axis_col'])
                main_chart = workbook.add_chart({'type' : sheet_chart_config['type']})
                for serie in sheet_chart_config['series']:
                    y_axis_col = data.columns.get_loc(serie['y_axis_col'])
                    serie_config = {
                        'name' : serie['name'],
                        'categories' : [name, 1, x_axis_col, len(data), x_axis_col],
                        'values' : [name, 1, y_axis_col, len(data), y_axis_col]
                    }
                    if 'fill' in serie:
                        serie_config['fill'] = {'color' : serie['fill']}

                    if 'line_color' in serie:
                        serie_config['line'] = {'color' : serie['line_color']}

                    if 'border' in serie:
                        serie_config['border'] = {'color' : serie['border']['color'], 'width' : serie['border']['width']} 
                    
                    if 'data_labels' in serie:
                        dl_config = serie['data_labels']
                        serie_config['data_labels'] = {k : v for k,v in dl_config.items() if k in options_labels}
                        if 'font' in dl_config:
                            serie_config['data_labels']['font'] = {'bold' : True}

                    if serie.get('type') == 'line':
                        chart_line = workbook.add_chart({'type' : 'line'})
                        if serie.get('y2_axis'):
                            serie_config['y2_axis'] = True
                        if serie.get('marker'):
                            m_config = serie['marker']
                            serie_config['marker'] = {k : v for k,v in m_config.items() if k in options_marker}
                            if 'fill' in m_config:
                                serie_config['marker']['fill'] = {'color' : m_config['fill']['color']}
                            if 'border' in m_config:
                                serie_config['marker']['border'] = {'color' : m_config['border']['color']}
                        chart_line.add_series(serie_config)
                        chart_line.set_y2_axis({
                            'visible': True,
                            'major_tick_mark': 'none',
                            'minor_tick_mark': 'none',
                            'num_font': {'color': '#FFFFFF'},
                            'line': {'none': True},
                            'major_gridlines': {'visible': False}
                        })
                        main_chart.combine(chart_line)
                    else:
                        main_chart.add_series(serie_config)

                
                
                main_chart.set_y_axis({
                        'visible': True,
                        'major_tick_mark': 'none',
                        'minor_tick_mark': 'none',
                        'num_font': {'color': '#FFFFFF'},
                        'line': {'none': True},
                        'major_gridlines': {'visible': False}
                    })
                
                main_chart.set_size({'width': 700, 'height': 500})
                main_chart.set_legend({'position' : 'none'})
                main_chart.set_title({'name' : sheet_chart_config['title']})
                worksheet.insert_chart(1, data.shape[1] + 1, main_chart)
                logger.info(f"Graphique créé avec pour la feuille {name}")



            
















                