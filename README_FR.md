# Python API Client Lab

Projet d’apprentissage Python progressif consacré à la consommation d’APIs HTTP avec `requests`, au traitement de réponses JSON, à l’analyse de données API, à la génération de rapports locaux et aux tests unitaires avec `pytest`.

Le projet commence par des exercices isolés, puis se termine par un refactor en package Python structuré avec une architecture `src/` et une suite de tests dédiée.

## Objectifs du projet

Ce projet a été conçu pour consolider les bases de la consommation d’API en Python, puis renforcer le code grâce à une architecture modulaire et à des tests unitaires.

Il couvre :

```text
- les bases des requêtes HTTP
- les requêtes GET
- les codes de statut HTTP
- la lecture de réponses JSON
- les query parameters
- les headers HTTP
- les requêtes POST avec payload JSON
- les timeouts
- la gestion d’erreurs API simple
- les fonctions client API réutilisables
- la sauvegarde de données API dans des fichiers locaux
- le refactor d’un script en package Python structuré
- l’écriture de tests unitaires avec pytest
```

## Fonctionnalités

```text
- récupérer des produits depuis l’API DummyJSON
- envoyer des paramètres de requête comme limit et skip
- lire et traiter des réponses JSON
- calculer le prix moyen des produits
- trouver le produit le plus cher
- trouver le produit avec le stock le plus bas
- générer un rapport texte à partir des données API
- sauvegarder le rapport avec pathlib
- organiser le code final dans un package réutilisable
- tester le comportement du package avec pytest
```

## Structure du projet

```text
python-api-http-requests-lab/
├── exercises/
│   ├── exercise_01_http_basics.py
│   ├── exercise_02_get_request.py
│   ├── exercise_03_status_code.py
│   ├── exercise_04_json_response.py
│   ├── exercise_05_query_params.py
│   ├── exercise_06_headers.py
│   ├── exercise_07_post_json.py
│   ├── exercise_08_timeout.py
│   ├── exercise_09_error_handling.py
│   ├── exercise_10_api_client_function.py
│   ├── exercise_11_save_api_data.py
│   └── exercise_12_api_report_generator.py
├── src/
│   └── api_client_lab/
│       ├── __init__.py
│       ├── client.py
│       ├── analyzer.py
│       ├── report.py
│       ├── writer.py
│       └── main.py
├── tests/
│   ├── test_analyzer.py
│   ├── test_client.py
│   ├── test_report.py
│   └── test_writer.py
├── data/
│   └── output/
│       └── reports/
│           └── api_products_report.txt
├── requirements.txt
├── pyproject.toml
├── README.md
└── README_FR.md
```

## Architecture du package

Le package final est organisé par responsabilité :

```text
client.py   → gère les appels API avec requests
analyzer.py → analyse les données produits
report.py   → construit le contenu du rapport texte
writer.py   → écrit le rapport avec pathlib
main.py     → orchestre le programme
```

Cette structure rend le code plus lisible, plus maintenable, plus testable et plus facile à faire évoluer.

## Prérequis

```text
Python 3.x
requests
pytest
```

Installation des dépendances :

```bash
pip install -r requirements.txt
```

## Exécution

Depuis la racine du projet, exécuter le package refactorisé avec :

```bash
PYTHONPATH=src python -m api_client_lab.main
```

Résultat attendu dans le terminal :

```text
API products report generated:
data/output/reports/api_products_report.txt
```

## Rapport généré

Le rapport généré contient :

```text
- le nombre total de produits disponibles côté API
- le nombre de produits reçus
- les valeurs limit et skip utilisées
- le prix moyen des produits
- le produit le plus cher
- le produit avec le stock le plus bas
- la liste formatée des produits reçus
```

Chemin du rapport généré :

```text
data/output/reports/api_products_report.txt
```

## Tests

Le projet contient une suite de tests pytest couvrant les principales responsabilités du package :

```text
test_analyzer.py → teste les fonctions d’analyse pures, les cas limites, parametrize, fixtures et erreurs attendues
test_report.py   → teste la génération du rapport texte via les informations importantes du contenu
test_writer.py   → teste l’écriture fichier avec tmp_path sans polluer les vrais dossiers du projet
test_client.py   → teste le client API avec monkeypatch sans appeler la vraie API
```

Lancer tous les tests depuis la racine du projet :

```bash
PYTHONPATH=src pytest -q
```

Pour un affichage détaillé :

```bash
PYTHONPATH=src pytest
```

La suite de tests actuelle valide :

```text
- les cas nominaux
- les cas limites
- les erreurs de champs manquants avec pytest.raises
- les comparaisons de nombres décimaux avec pytest.approx
- les cas répétés avec pytest.mark.parametrize
- les données de test réutilisables avec les fixtures pytest
- l’écriture dans des fichiers temporaires avec tmp_path
- la simulation du comportement API avec monkeypatch
```

## Compétences validées

Ce projet valide la capacité à :

```text
- consommer une API externe avec Python
- utiliser requests avec params, headers et timeout
- interpréter les codes de statut HTTP
- convertir une réponse JSON en dictionnaire Python
- traiter une liste de dictionnaires
- calculer des indicateurs simples
- générer un rapport à partir de données API
- sauvegarder des fichiers avec pathlib
- structurer du code Python en modules
- séparer les responsabilités dans un package
- exécuter un package avec python -m
- écrire des tests unitaires utiles avec pytest
- tester des fonctions pures, l’écriture fichier, la génération de rapport et le client API
- isoler les dépendances externes dans les tests avec monkeypatch
```

## Statut du projet

Le module principal API et le mini-module pytest sont terminés.

Blocs API validés :

```text
01 - Bases HTTP
02 - Première requête GET
03 - Codes de statut HTTP
04 - Réponse JSON
05 - Query parameters
06 - Headers
07 - POST JSON
08 - Timeouts
09 - Gestion d’erreurs
10 - Fonction client API réutilisable
11 - Sauvegarde de données API
12 - Mini-projet générateur de rapport API
13 - Refactor en package src
```

Blocs pytest validés :

```text
01 - Premiers tests unitaires avec pytest
02 - Cas limites et erreurs attendues
03 - Tests paramétrés avec pytest.mark.parametrize
04 - Fixtures avec pytest.fixture
05 - Test unitaire de génération de rapport
06 - Test d’écriture fichier avec tmp_path
07 - Tests du client API avec monkeypatch
08 - Consolidation de la suite de tests et documentation README
```

## Améliorations possibles

```text
- renforcer la gestion d’erreurs API
- déplacer l’URL de base de l’API dans une configuration
- filtrer les produits par catégorie
- exporter les rapports en JSON ou CSV
- ajouter GitHub Actions pour lancer pytest automatiquement
- ajouter un rapport de couverture de tests
- finaliser davantage le packaging avec pyproject.toml
```
