


import smtplib
from email.message import EmailMessage
from loguru import logger
from config import TODAY, SMTP_SERVER, SMTP_PORT, EXPEDITEUR, DESTINATAIRE, MDP, FILE_PATH_REPORT , TIMEOUT_SMTP
from pathlib import Path


def send_mail(status : bool, details : str, now : str = TODAY, smtp_server : str = SMTP_SERVER, smtp_port : int = SMTP_PORT, From : str = EXPEDITEUR, To : str = DESTINATAIRE, mdp : str = MDP, time_out : int = TIMEOUT_SMTP, file_path : str = FILE_PATH_REPORT) -> None:
    """
    Envoie des mails de notifications

    Args : 
        status : booleen 
        now : pour les horodatages
        smtp_server : le serveur SMTP
        smtp_port : le port du serveur SMTP
        From : l'expéditeur du mail
        To : le destinataire du mail
        mdp : le mots de passe de l'expéditeur

    Returns : 
        None : Juste envoie le mail 
    
    Raise : 


    """
    logger.info("Cette fonction s'occupe d'envoyer des emails de notifications une fois le pipeline exécuté")

    if not all ([From, To, mdp]):
        logger.error("Impossible d'envoyer le mail causes d'infos incomplet : Email non configuré")
        return
    
    if status:
        subject = "[Pipeline Ventes restaurant] ✅ SUCCÈS"
        corps = f"""
            🎉 PIPELINE TERMINÉ AVEC SUCCÈS | {now}
            📊 RÉSULTATS :
            {details}
        """
    else:
        subject = "[Pipeline Ventes restaurant] ❌ ÉCHEC"
        corps = f"""
            🚨 PIPELINE ÉCHOUÉ | {now}
            ⚠️ ERREUR :
            {details}
            📌 Vérifier les logs dans le dossier Logs
        """

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = From
    msg['To'] = To
    msg.set_content(corps.strip())


    if status and file_path:
        path_object = Path(file_path)
        if path_object.exists() and path_object.is_file():
            try:
                file_data = path_object.read_bytes()
                file_name = path_object.name
                msg.add_attachment(
                    file_data,
                    maintype = 'application',
                    subtype = 'octet-stream',
                    filename = file_name
                )
                logger.info(f"Fichier joint avec succès : {file_name}")
            except Exception as e:
                logger.error(f"Impossible d'attacher le fichier {path_object.name} : {e}")
        else:
            logger.warning(f"Le fichier spécifié est introuvable ou invalide : {file_path}")


    try:
        with smtplib.SMTP(smtp_server, smtp_port, timeout=time_out) as server:
            server.starttls()
            server.login(From, mdp)
            server.send_message(msg)
            logger.success(f"Email {subject} envoyé à {To} | {now}")
    except Exception as e:
        logger.error(f"Erreur lors de l'envoie du mail : {e}")

