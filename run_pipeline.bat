@echo off
:: 1. Aller dans le dossier de ton projet
cd /d "%~dp0"

:: 2. Activer ton environnement virtuel Python
call venv\scripts\activate

:: 3. Lancer ton pipeline principal
python main.py 

:: 4. Fermer automatiquement après exécution
exit




