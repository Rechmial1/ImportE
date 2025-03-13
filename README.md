# **ImportE - Outil d'importation de fichiers Excel dans une base de données SQLite en ligne de commande**

## **Description**

Ce projet permet de créer, importer et administrer une base de données SQLite à partir d'un fichier Excel. Il propose également diverses commandes permettant de lister les tables, d'afficher leur contenu et d'exécuter d'autres opérations, le tout via une interface en ligne de commande (CLI).

## **Installation**

### **Installation de Python 3 et de pip**

#### **Mise à jour des paquets**
Avant toute installation, assurez-vous que votre système est à jour en exécutant la commande suivante :

```bash
sudo apt update
```

#### **Installation de Python 3**
Python 3 est généralement inclus dans les dépôts officiels des distributions Linux. Pour l'installer, utilisez la commande suivante :

```bash
sudo apt install python3
```

#### **Installation de pip pour Python 3**
Une fois Python installé, vous pouvez installer pip, le gestionnaire de paquets de Python, en exécutant la commande suivante :

```bash
sudo apt install python3-pip
```

#### **Vérification de l'installation**
Après l’installation, il est recommandé de vérifier que Python et pip sont correctement installés en affichant leurs versions respectives :

```bash
python3 --version
pip3 --version
```

Si l'installation a été effectuée avec succès, vous devriez obtenir un affichage similaire à celui-ci :

```bash
Python 3.x.x
pip 20.x.x
```

---

## **Clonage du dépôt**

```bash
git clone https://github.com/Rechmial1/ImportE.git
```

### **Accès au répertoire du projet**
```bash
cd ImportE
```

### **Création d'un environnement virtuel**
```bash
python3 -m venv venv
```
Cette commande génère un répertoire `venv` contenant toutes les dépendances isolées nécessaires au projet.

### **Activation de l'environnement virtuel**
Une fois l’environnement virtuel créé, il est impératif de l’activer avant d’installer les dépendances requises.

```bash
source venv/bin/activate
```

---

## **Installation des dépendances**
```bash
pip install -r requirements.txt
```

---

## **Utilisation**

### **Exécution du script en ligne de commande (sans alias)**
Pour l'exécution sans alias vous devez soit être dans le dossier du projet soit avoir le chemain absolu du fichier main.py
## Dans notre cas on considère que nous sommes dans le dossier du projet
#### **Création d'une table**
```bash
python3 main.py create --db <nom_db> --table <nom_table> --columns <colonne1:type1> <colonne2:type2> ...
```
**Exemple :**
```bash
python3 main.py create --db personnes --table utilisateurs --columns matricule:TEXT nom:TEXT prenom:TEXT date_naissance:DATE status:TEXT
```

#### **Types de données valides**
Les types de données acceptés pour les colonnes sont : `TEXT`, `INTEGER`, `REAL`, `BLOB`, `DATE`.

#### **Importation d’un fichier Excel dans une table**
```bash
python3 main.py import --db <nom_db> --table <nom_table> --file <chemin_fichier_excel>
```
**Exemple :**
```bash
python3 main.py import --db personnes --table utilisateurs --file /chemin/vers/fichier.xlsx
```

#### **Suppression d'une table**
```bash
python3 main.py delete --db <nom_db> --table <nom_table>
```
**Exemple :**
```bash
python3 main.py delete --db personnes --table utilisateurs
```

#### **Suppression de la base de données**
```bash
python3 main.py delete-db --db <nom_db>
```
**Exemple :**
```bash
python3 main.py delete-db --db personnes
```

#### **Affichage de la liste des tables**
```bash
python3 main.py list-tables --db <nom_db>
```
**Exemple :**
```bash
python3 main.py list-tables --db personnes
```

#### **Affichage du contenu d'une table**
```bash
python3 main.py view --db <nom_db> --table <nom_table>
```
**Exemple :**
```bash
python3 main.py view --db personnes --table utilisateurs
```

#### **Affichage de la structure d'une table (DESCRIBE)**
```bash
python3 main.py describe --db <nom_db> --table <nom_table>
```
**Exemple :**
```bash
python3 main.py describe --db personnes --table utilisateurs
```

---

## **Exécution du script avec un alias**

### **Rendre le script exécutable**
Avant de pouvoir utiliser un alias, il est nécessaire de rendre le script exécutable :

```bash
chmod +x main.py
```

### **Création d'un alias pour simplifier l’exécution du script**
Si vous souhaitez exécuter le script avec une commande plus concise, comme `importE`, vous pouvez définir un alias dans votre fichier de configuration Shell (`~/.bashrc` ou `~/.zshrc`).

Ouvrez le fichier de configuration avec un éditeur de texte :  
```bash
nano ~/.bashrc
```

Ajoutez la ligne suivante à la fin du fichier :  
```bash
alias importE="python3 /chemin/vers/ton/projet/importE/main.py"
```

Rechargez ensuite le fichier de configuration pour appliquer les modifications :  
```bash
source ~/.bashrc
```

---

### **Activation de l’environnement virtuel**
Avant d'exécuter toute commande, assurez-vous d'activer l'environnement virtuel :

```bash
source venv/bin/activate
```

### **Exécution du script avec l’alias**
Une fois l’alias configuré, il est possible d’exécuter les commandes en utilisant `importE` directement.

**Exemple :**  
```bash
importE create --db ma_base --table ma_table --columns nom:TEXT age:INTEGER
```
