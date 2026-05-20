![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![XlsxWriter](https://img.shields.io/badge/XlsxWriter-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Loguru](https://img.shields.io/badge/Loguru-000000?style=for-the-badge&logo=python&logoColor=white)
![psycopg2](https://img.shields.io/badge/psycopg2-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![python-dotenv](https://img.shields.io/badge/python--dotenv-ECD53F?style=for-the-badge&logo=dotenv&logoColor=black)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

# 📊 End-to-End 🍽️ Pipeline ETL — Analyse des Ventes Restaurant

### PostgreSQL → Python → PostgreSQL → Excel → Power BI Dashboard

Pipeline ETL complet et automatisé pour l'analyse des ventes d'un réseau de 10 restaurants français.  
Les données brutes CSV sont extraites depuis PostgreSQL, nettoyées, enrichies, réinjectées en base propre, puis restituées via un rapport Excel multi-onglets avec graphiques et un dashboard Power BI connecté directement à la base.

---

## 📊 Aperçu des résultats

| Indicateur | Valeur |
|---|---|
| Lignes brutes | 12 000 |
| Doublons supprimés | 4 335 |
| Lignes nettoyées | 7 665 |
| CA Total | 133 010 € |
| Quantité vendue | 11 000+ |
| Discount moyen | 6,47 % |
| Restaurants analysés | 10 |
| Plats analysés | 10 |
| Temps d'exécution pipeline | ~6,7 secondes |

---

## 🏗️ Architecture du Pipeline

```
PostgreSQL (données brutes)
        ↓
extract.py          — Extraction + retry exponentiel (3 tentatives)
        ↓
clean.py            — Nettoyage robuste (regex, encodage, types stricts)
        ↓
features.py         — Enrichissement (total_price, discount_amount, total_amount, service_type)
        ↓
injection_data_to_sql.py  — TRUNCATE RESTART IDENTITY + execute_batch (page_size=1000)
        ↓
analysis_*.py       — 3 axes d'analyse (restaurant, plat, catégorie)
        ↓
repport_excel.py    — Rapport Excel config-driven (graphiques + mise en forme conditionnelle)
        ↓
Power BI            — Dashboard connecté directement à PostgreSQL
```

---

## 📁 Structure du projet

```
pipeline-ventes-restaurant/
├── images/
│   ├── Rapport_Excel/              # 📸 Captures d'écran du rapport Excel
│   ├── Dashbord_Power_BI/          # 📸 Captures d'écran du dashboard
│   └── Diagramme_Architecture/     # 🏗️ Diagramme d'architecture
|
├── reports/
│   └── rapport_analyse_vente_restaurant.pdf  # 📄 Rapport d'analyse complet
|
├── src/
|   ├── analysis/
|   |   ├── __init__.py
|   |   ├── analysis_restaurant.py      # Analyse par restaurant
│   |   ├── analysis_plats.py           # Analyse par plat
│   |   ├── analysis_category.py        # Analyse par catégorie + Impact CA%
│   ├── __init__.py
│   ├── extract.py                  # Extraction PostgreSQL avec retry
│   ├── clean.py                    # Nettoyage (regex, types, doublons)
│   ├── features.py                 # Feature engineering
│   ├── injection_data_to_sql.py    # Injection PostgreSQL (execute_batch)
│   ├── repport_excel.py            # Rapport Excel config-driven
│   └── logging.py                  # Configuration Loguru centralisée
├── tests/
│   ├── __init__.py
│   ├── test_clean_data.py          # ✅ Tests unitaires nettoyage
│   └── test_add_features.py        # ✅ Tests unitaires features
│
├── data/
│   ├── raw/                        # Échantillon CSV brut (10 lignes)
│   └── processed/                  # Échantillon CSV nettoyé (10 lignes)
│
├── Output/                         # Rapport Excel généré (horodaté)
|
├── Logs/                           # Fichiers de logs (rotation 10MB, 30 jours)
|
├── power_bi/                       # Dashboard Power BI (.pbix)
│       └── dashboard_ventes_janvier.pbix
|
├── config.py                       # Configuration centralisée (chemins, DB, Excel, graphiques)
├── main.py                         # Point d'entrée du pipeline
├── .env                            # Credentials PostgreSQL (non versionné)
├── .env.example                    # Template credentials
├── .gitignore
└── README.md
```

---

## ⚙️ Configuration — `config.py`

Toute la configuration est centralisée dans `config.py` :

- **Connexion PostgreSQL** via `dotenv_values(".env")` — credentials jamais exposés
- **Chemins** via `pathlib.Path` avec création automatique des dossiers
- **`EXCEL_FORMATTING`** — dictionnaire de dictionnaires (feuille → colonne → seuils) pour la mise en forme conditionnelle
- **`EXCEL_CHARTS`** — configuration complète des graphiques (type, séries, couleurs, data labels, markers)
- **`EXCLUDED_SHEETS`** — feuilles exclues du formatage

```python
# Exemple EXCEL_FORMATTING
EXCEL_FORMATTING = {
    'Données Par Restaurant': {
        'total_amount': {'red_value': 15, 'min_orange': 15, 'max_orange': 40, 'green_value': 40},
        'discount':     {'red_value': 5,  'min_orange': 6,  'max_orange': 15, 'green_value': 15}
    },
    ...
}
```

---

## 🔧 Modules détaillés

### `extract.py` — Extraction
- Connexion PostgreSQL via `psycopg2`
- **Retry exponentiel** : 3 tentatives, délai x2 à chaque échec
- Sauvegarde d'un échantillon de contrôle (10 lignes) en CSV local
- `sys.exit()` si toutes les tentatives échouent

### `clean.py` — Nettoyage
- Suppression des doublons avec log dynamique du nombre supprimé
- **Regex optimisée** sur `unit_price` : `r"(\d+[\,.]?\d*)"` — extrait la partie numérique, gère `€`, espaces, bugs d'encodage (`â¬`)
- **Regex optimisée** sur `discount` : `r"(\d+)"` — extrait les chiffres, ignore `%`
- `pd.to_numeric(errors='coerce')` sur toutes les colonnes numériques — zéro plantage
- `downcast='integer'` sur `quantity` pour économie mémoire
- Dates : `format='mixed'` + `dayfirst=True` pour formats européens mixtes
- Heures : `format='mixed'` pour `HH:MM` et `HH:MM:SS`
- Export d'un échantillon de 10 lignes (contrôle qualité GitHub)

### `features.py` — Enrichissement
| Colonne créée | Calcul |
|---|---|
| `total_price` | `unit_price × quantity` |
| `discount_amount` | `total_price × discount / 100` |
| `total_amount` | `total_price − discount_amount` |
| `service_type` | `"Soir"` si heure ≥ 19h, sinon `"Dejeuner"` |

### `injection_data_to_sql.py` — Injection PostgreSQL
- Vérification `df.empty` avant injection
- `TRUNCATE TABLE ... RESTART IDENTITY` — remet le compteur SERIAL à 1
- `execute_batch(cur, query, data, page_size=1000)` — 12 batchs de 1000 lignes
- Colonnes dynamiques depuis `df.columns` — pas d'id hardcodé

### `analysis_*.py` — Analyses
- **Par restaurant** : CA, quantité, discount moyen, rating moyen — trié par `total_amount` DESC
- **Par plat** : prix unitaire, quantité, discount moyen, rating, CA calculé avec discount
- **Par catégorie** : agrégats + `Impact_CA_%` = part de chaque catégorie dans le CA total

### `repport_excel.py` — Rapport Excel
- Architecture **config-driven** : toute la logique de formatage et graphiques est dans `config.py`
- Freeze panes, autofilter, headers colorés sur toutes les feuilles traitées
- Ajustement automatique de la largeur des colonnes
- Formats monétaires (`#,##0.00 €`), pourcentages, notes (`0" / 5"`)
- Mise en forme conditionnelle (rouge / orange / vert) par feuille et par colonne
- **Graphiques combinés** (colonne + ligne) avec axe Y secondaire pour le rating
- Camembert pour la répartition par plat
- Détection automatique du type de graphique via `serie.get('type') == 'line'`

---

## 📈 Dashboard Power BI

Connexion directe à PostgreSQL via le pilote **Npgsql v4.1.3** (GAC Installation) :

| Visual | Description |
|---|---|
| 4 KPI Cards | CA Total · Quantité · Discount Total · Discount Moyen |
| Barres par restaurant | CA par restaurant avec filtre dynamique |
| Barres par mois | Évolution mensuelle du CA (janvier → mai 2024) |
| Camembert par restaurant | Répartition du CA (% par restaurant) |
| Barres par ID | Vue granulaire par identifiant restaurant |
| Filtres | Date · Restaurant · Menu · Service Type |

---

## 🚀 Installation & Lancement

### Prérequis
- Python 3.11+
- PostgreSQL 15+
- Power BI Desktop (optionnel)

### Installation

```bash
git clone https://github.com/SopeTaha92/pipeline-ventes-restaurant
cd pipeline-ventes-restaurant
pip install -r requirements.txt
```

### Configuration

```bash
cp .env.example .env
# Éditer .env avec vos credentials PostgreSQL
```

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=votre_base
DB_USER=postgres
DB_PASSWORD=votre_mot_de_passe
DB_TABLE=vente_restaurant_brut
DB_TABLE_COMPLET=vente_restaurant_12K_clean
```

### Lancement

```bash
python main.py
```

Le rapport Excel est généré automatiquement dans `Output/vente_restaurant_DD-MM-YYYY_HH-MM.xlsx`.

---

## 📦 Dépendances

```
pandas
psycopg2-binary
python-dotenv
loguru
xlsxwriter
```

---

## ⚠️ Limitations

> Données synthétiques générées par IA — 4 335 doublons détectés et supprimés sur 12 000 lignes initiales.  
> Certains `unit_price` peuvent être à 0 (artefact de la génération IA) — les contraintes SQL ont été adaptées en conséquence (`>= 0` au lieu de `> 0`).

---

## 👤 Auteur

**Mahmoud At-Tidiane**  
Data Analyst · Dakar, Sénégal  
🔗 [github.com/SopeTaha92](https://github.com/SopeTaha92)
