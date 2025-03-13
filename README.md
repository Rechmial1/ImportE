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
   Exécutez le script avec Python pour utiliser les commandes suivantes ( Sans l'utilisation d'alias )  :
   
1. Créer une table :
   ```bash
   python importE/main.py create --db <nom_db> --table <nom_table> --columns <colonne1:type1> <colonne2:type2> ...
   ```
   Exemple : python importE/main.py create --db personnes --table utilisateurs --columns matricule:TEXT nom:TEXT prenom:TEXT date_naissance:DATE status:TEXT

3. Types de données valides :
   Les types valides pour les colonnes sont : TEXT, INTEGER, REAL, BLOB, DATE

4. Importer un fichier Excel dans une table :
   ```bash
   python importE/main.py import --db <nom_db> --table <nom_table> --file <chemin_fichier_excel>
   ```
   Exemple : python importE/main.py import --db personnes --table utilisateurs --file /chemin/vers/fichier.xlsx

6. Supprimer une table :
   ```bash
   python importE/main.py delete --db <nom_db> --table <nom_table>
   ```
   Exemple : python importE/main.py delete --db personnes --table utilisateurs

8. Supprimer la base de données :
   ```bash
   python importE/main.py delete-db --db <nom_db>
   ```
   Exemple : python importE/main.py delete-db --db personnes

10. Lister les tables :
    ```bash
    python importE/main.py list-tables --db <nom_db>
    ```
   Exemple : python importE/main.py list-tables --db personnes

12. Voir le contenu d'une table :
    ```bash
    python importE/main.py view --db <nom_db> --table <nom_table>
    ```
   Exemple : python importE/main.py view --db personnes --table utilisateurs

14. Voir la structure d'une table (DESCRIBE) :
    ```bash
    python importE/main.py describe --db <nom_db> --table <nom_table>
    ```
   Exemple : python importE/main.py describe --db personnes --table utilisateurs


Exécutez le script avec Python pour utiliser les commandes suivantes ( Avec l'utilisation d'alias )  :

Rendre le fichier exécutable
1. Dans ton terminal, donne les permissions d'exécution à ton script :

```bash
chmod +x importE/main.py
```
2. Créer un alias pour exécuter le script avec une commande courte
Si tu veux pouvoir exécuter ton script avec une commande plus courte comme importE, tu peux ajouter un alias dans ton fichier ~/.bashrc ou ~/.zshrc (selon ton shell) :

Ouvre ton fichier .bashrc (ou .zshrc) avec un éditeur de texte :
```bash
nano ~/.bashrc
```
Ajoute cette ligne à la fin du fichier :
```bash
alias importE="python3 /chemin/vers/ton/projet/importE/main.py"
```
Puis recharge ton fichier de configuration :
```bash
source ~/.bashrc
```
Désormais, tu peux exécuter ton script en utilisant simplement importE :

Exemple : importE create --db ma_base --table ma_table --columns nom:TEXT age:INTEGER
