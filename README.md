# importE - Outil de gestion de base de données SQLite en ligne de commande

## Description

Ce projet permet de créer, importer, et gérer une base de données SQLite via un fichier Excel. Il offre aussi des commandes pour lister les tables, afficher leur contenu et plus encore, tout cela via une interface en ligne de commande (CLI).

## Installation

## Installer Python 3 et pip :
   ## Mettre à jour les paquets :
   ````bash
   sudo apt update
   ````
   ## Installer Python 3 :
   Python 3 est généralement inclus dans les dépôts par défaut. Installe-le avec la commande suivante :
   ````bash
   sudo apt install python3
   ````
   ## Installer pip pour Python 3 :
   Une fois Python installé, tu peux installer pip (le gestionnaire de paquets pour Python) avec la commande suivante :
   ````bash
   sudo apt install python3-pip
   ````
   ## Vérifier l'installation :
   Une fois l'installation terminée, tu peux vérifier que Python et pip sont correctement installés en vérifiant leurs versions :
   ````bash
   python3 --version
   pip3 --version
   ````
   Si tout est installé correctement, cela te donnera quelque chose comme :
   ````bash
   Python 3.x.x
   pip 20.x.x
   ````

## Clonez ce dépôt :
   ```bash
   git clone https://github.com/Rechmial1/ImportE.git
   ```
   ## Aller dans le dossier 
   ```bash
   cd ImportE
   ````
   ## Crée un environnement virtuel :
   ````bash 
   python3 -m venv venv
   ````
   Cela créera un répertoire venv dans lequel toutes les dépendances seront installées.

   ## Active l'environnement virtuel :
   Une fois l'environnement créé, active-le pour pouvoir installer les dépendances dans cet environnement isolé.
   ````bash
   source venv/bin/activate
   ````
## Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ````

## Utilisation : Cas 1
   ## Exécutez le script avec Python pour utiliser les commandes suivantes ( Sans l'utilisation d'alias )  :
   
   1. Créer une table :
      ```bash
      python3 main.py create --db <nom_db> --table <nom_table> --columns <colonne1:type1> <colonne2:type2> ...
      ```
      Exemple : python3 main.py create --db personnes --table utilisateurs --columns matricule:TEXT nom:TEXT prenom:TEXT date_naissance:DATE status:TEXT

   3. Types de données valides :
      Les types valides pour les colonnes sont : TEXT, INTEGER, REAL, BLOB, DATE

   4. Importer un fichier Excel dans une table :
      ```bash
      python3 main.py import --db <nom_db> --table <nom_table> --file <chemin_fichier_excel>
      ```
      Exemple : python3 main.py import --db personnes --table utilisateurs --file /chemin/vers/fichier.xlsx

   6. Supprimer une table :
      ```bash
      python3 main.py delete --db <nom_db> --table <nom_table>
      ```
      Exemple : python3 main.py delete --db personnes --table utilisateurs

   8. Supprimer la base de données :
      ```bash
      python3 main.py delete-db --db <nom_db>
      ```
      Exemple : python3 main.py delete-db --db personnes

   10. Lister les tables :
       ```bash
       python3 main.py list-tables --db <nom_db>
       ```
   Exemple : python3 main.py list-tables --db personnes

   12. Voir le contenu d'une table :
       ```bash
       python3 main.py view --db <nom_db> --table <nom_table>
       ```
   Exemple : python3 main.py view --db personnes --table utilisateurs

   14. Voir la structure d'une table (DESCRIBE) :
       ```bash
       python3 main.py describe --db <nom_db> --table <nom_table>
       ```
   Exemple : python3 main.py describe --db personnes --table utilisateurs


## Exécutez le script avec Python pour utiliser les commandes suivantes ( Avec l'utilisation d'alias )  :
Rendre le fichier exécutable
1. Dans ton terminal, donne les permissions d'exécution à ton script :

```bash
chmod +x main.py
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

   ## Aller dans le dossier 
   ```bash
   cd ImportE
   ````
   Cela créera un répertoire venv dans lequel toutes les dépendances seront installées.

   ## Active l'environnement virtuel :
   Une fois l'environnement créé, active-le pour pouvoir installer les dépendances dans cet environnement isolé.
   ````bash
   source venv/bin/activate
   ````

Désormais, tu peux exécuter ton script en utilisant simplement importE :

Exemple : importE create --db ma_base --table ma_table --columns nom:TEXT age:INTEGER
