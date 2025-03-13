# importE - Outil de gestion de base de données SQLite en ligne de commande

## Description

Ce projet permet de créer, importer, et gérer une base de données SQLite via un fichier Excel. Il offre aussi des commandes pour lister les tables, afficher leur contenu et plus encore, tout cela via une interface en ligne de commande (CLI).

## Installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/Rechmial1/ImportE.git
2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
3. Utilisation
   Exécutez le script avec Python pour utiliser les commandes suivantes :
   
A. Créer une table :
   ```bash
   python importE/main.py create --db ma_base --table ma_table --columns nom:TEXT age:INTEGER
   ```
B. Importer un fichier Excel :
   ```bash
   python importE/main.py import --db ma_base --table ma_table --file chemin/vers/fichier.xlsx
   ```
C. Lister les tables :
   ```bash
   python importE/main.py list --db ma_base
   ```
D. Afficher le contenu d'une table :
   ```bash
   python importE/main.py describe --db ma_base --table ma_table
