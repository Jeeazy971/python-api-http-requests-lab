# Python API Client Lab

Projet d’apprentissage Python progressif consacré à la consommation d’APIs HTTP avec `requests`, au traitement de réponses JSON, à l’analyse de données API et à la génération de rapports locaux.

Le projet commence par des exercices isolés, puis se termine par un refactor en package Python structuré avec une architecture `src/`.

## Objectifs du projet

Ce projet a été conçu pour consolider les bases de la consommation d’API en Python.

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
```

## Statut du projet

Le module principal d’apprentissage est terminé.

Blocs validés :

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

## Améliorations possibles

```text
- ajouter des tests unitaires
- renforcer la gestion d’erreurs
- déplacer l’URL de base de l’API dans une configuration
- filtrer les produits par catégorie
- exporter les rapports en JSON ou CSV
- finaliser le packaging avec pyproject.toml
```
