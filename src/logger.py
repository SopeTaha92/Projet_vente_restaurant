



from loguru import logger


def logger_file(file : str):
    """Cette fonction se charge de la création des fichiers de logs"""
    logger.remove()
    logger.add(
        file,
        rotation='10 MB',
        retention='30 days',
        compression='zip',
        level='INFO',
        format='{time:YYYY-MM-DD HH-mm-ss} | {level} | {name}:{line} | {message}'

    )
    logger.info('Création du fichier de log avec succée')