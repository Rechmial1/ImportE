import argparse
import sqlite3
import pandas as pd
import os
import time

# Liste des types valides de SQLite
VALID_TYPES = ['TEXT', 'INTEGER', 'REAL', 'BLOB', 'DATE']

def create_table(db_name, table_name, columns):
    # Crée une table dans la base de données SQLite avec les colonnes spécifiées par l'utilisateur
    start_time = time.time()  # Mesure du temps de départ

    # Vérification des types des colonnes
    for col in columns:
        col_name, col_type = col.split(":")
        if col_type.upper() not in VALID_TYPES:
            print(f"ERREUR : Le type '{col_type}' pour la colonne '{col_name}' est invalide. Types valides : {', '.join(VALID_TYPES)}.")
            return

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Générer la définition des colonnes à partir des paramètres d'entrée
    columns_def = ', '.join([f'{col.split(":")[0]} {col.split(":")[1]}' for col in columns])
    query = f'CREATE TABLE IF NOT EXISTS {table_name} ({columns_def});'

    # Exécuter la requête
    cursor.execute(query)
    conn.commit()
    conn.close()

    end_time = time.time()  # Mesure du temps de fin
    print(f"Table '{table_name}' créée avec succès dans '{db_name}'.")
    print(f"Temps d'exécution pour la création : {end_time - start_time:.2f} secondes.")

def import_excel(db_name, table_name, file_path):
    # Importe un fichier Excel dans une table SQLite
    start_time = time.time()  # Mesure du temps de départ

    if not os.path.exists(file_path):
        print("Fichier introuvable !")
        return

    conn = sqlite3.connect(db_name)
    df = pd.read_excel(file_path)

    # Vérification et traitement des données
    df = df.map(lambda x: float(x) if isinstance(x, int) and x > 9_223_372_036_854_775_807 else x)

    # Insertion des données dans la table SQLite
    df.to_sql(table_name, conn, if_exists='append', index=False)
    conn.close()

    end_time = time.time()  # Mesure du temps de fin
    print(f"Données importées avec succès dans la table '{table_name}'.")
    print(f"Temps d'exécution pour l'importation : {end_time - start_time:.2f} secondes.")

def delete_table(db_name, table_name):
    # Supprime une table dans la base de données SQLite
    start_time = time.time()  # Mesure du temps de départ

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    query = f'DROP TABLE IF EXISTS {table_name};'
    cursor.execute(query)
    conn.commit()
    conn.close()

    end_time = time.time()  # Mesure du temps de fin
    print(f"Table '{table_name}' supprimée avec succès de la base '{db_name}'.")
    print(f"Temps d'exécution pour la suppression : {end_time - start_time:.2f} secondes.")

def delete_db(db_name):
    # Supprime la base de données SQLite
    start_time = time.time()  # Mesure du temps de départ

    if os.path.exists(db_name):
        os.remove(db_name)
        end_time = time.time()  # Mesure du temps de fin
        print(f"Base de données '{db_name}' supprimée avec succès.")
        print(f"Temps d'exécution pour la suppression : {end_time - start_time:.2f} secondes.")
    else:
        print(f"ERREUR : La base de données '{db_name}' n'existe pas.")

def list_tables(db_name):
    # Liste les tables présentes dans la base de données SQLite
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    query = "SELECT name FROM sqlite_master WHERE type='table';"
    cursor.execute(query)
    tables = cursor.fetchall()

    if tables:
        print("Tables présentes dans la base de données :")
        for table in tables:
            print(table[0])
    else:
        print(f"Aucune table trouvée dans la base de données '{db_name}'.")
    conn.close()

def view_table(db_name, table_name):
    # Affiche le contenu d'une table dans la base de données SQLite
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    query = f'SELECT * FROM {table_name};'
    cursor.execute(query)
    rows = cursor.fetchall()

    if rows:
        print(f"Contenu de la table '{table_name}' :")
        for row in rows:
            print(row)
    else:
        print(f"Aucune donnée trouvée dans la table '{table_name}'.")
    conn.close()

def describe_table(db_name, table_name):
    # Affiche la structure des colonnes d'une table dans la base de données SQLite
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    query = f'PRAGMA table_info({table_name});'
    cursor.execute(query)
    columns = cursor.fetchall()

    if columns:
        print(f"Structure de la table '{table_name}' :")
        for col in columns:
            print(f"Colonne : {col[1]}, Type : {col[2]}")
    else:
        print(f"Aucune structure trouvée pour la table '{table_name}'.")
    conn.close()

def show_help():
    # Affiche un message d'aide pour chaque commande
    print("Utilisation des commandes :")
    print("\n1. Créer une table :")
    print("   create --db <nom_db> --table <nom_table> --columns <colonne1:type1> <colonne2:type2> ...")
    print("   Exemple : create --db personnes --table utilisateurs --columns matricule:TEXT nom:TEXT prenom:TEXT date_naissance:DATE status:TEXT")
    
    # Liste des types valides
    print("\n2. Types de données valides :")
    print(f"   Les types valides pour les colonnes sont : {', '.join(VALID_TYPES)}")

    print("\n3. Importer un fichier Excel dans une table :")
    print("   import --db <nom_db> --table <nom_table> --file <chemin_fichier_excel>")
    print("   Exemple : import --db personnes --table utilisateurs --file /chemin/vers/fichier.xlsx")

    print("\n4. Supprimer une table :")
    print("   delete --db <nom_db> --table <nom_table>")
    print("   Exemple : delete --db personnes --table utilisateurs")

    print("\n5. Supprimer la base de données :")
    print("   delete-db --db <nom_db>")
    print("   Exemple : delete-db --db personnes")

    print("\n6. Lister les tables :")
    print("   list-tables --db <nom_db>")
    print("   Exemple : list-tables --db personnes")

    print("\n7. Voir le contenu d'une table :")
    print("   view --db <nom_db> --table <nom_table>")
    print("   Exemple : view --db personnes --table utilisateurs")

    print("\n8. Voir la structure d'une table (DESCRIBE) :")
    print("   describe --db <nom_db> --table <nom_table>")
    print("   Exemple : describe --db personnes --table utilisateurs")

def main():
    # Point d'entrée de l'application en ligne de commande
    parser = argparse.ArgumentParser(description="Gestion de base de données SQLite en ligne de commande")
    subparsers = parser.add_subparsers(dest='command')

    # Commande CREATE
    create_parser = subparsers.add_parser('create', help='Créer une table dans la base de données')
    create_parser.add_argument('--db', required=True, help='Nom de la base de données')
    create_parser.add_argument('--table', required=True, help='Nom de la table à créer')
    create_parser.add_argument('--columns', required=True, nargs='+', help='Colonnes de la table (ex: matricule:TEXT nom:TEXT prenom:TEXT date_naissance:DATE status:TEXT)')

    # Commande IMPORT
    import_parser = subparsers.add_parser('import', help='Importer un fichier Excel dans une table SQLite')
    import_parser.add_argument('--db', required=True, help='Nom de la base de données')
    import_parser.add_argument('--table', required=True, help='Nom de la table où importer les données')
    import_parser.add_argument('--file', required=True, help='Chemin du fichier Excel')

    # Commande DELETE (Table)
    delete_parser = subparsers.add_parser('delete', help='Supprimer une table de la base de données')
    delete_parser.add_argument('--db', required=True, help='Nom de la base de données')
    delete_parser.add_argument('--table', required=True, help='Nom de la table à supprimer')

    # Commande DELETE (Base de données)
    delete_db_parser = subparsers.add_parser('delete-db', help='Supprimer la base de données SQLite')
    delete_db_parser.add_argument('--db', required=True, help='Nom de la base de données')

    # Commande LIST (Tables)
    list_parser = subparsers.add_parser('list-tables', help='Lister toutes les tables de la base de données')
    list_parser.add_argument('--db', required=True, help='Nom de la base de données')

    # Commande VIEW (Voir le contenu d’une table)
    view_parser = subparsers.add_parser('view', help='Voir le contenu d’une table dans la base de données')
    view_parser.add_argument('--db', required=True, help='Nom de la base de données')
    view_parser.add_argument('--table', required=True, help='Nom de la table à afficher')

    # Commande DESCRIBE (Structure d’une table)
    describe_parser = subparsers.add_parser('describe', help='Voir la structure d’une table (DESCRIBE)')
    describe_parser.add_argument('--db', required=True, help='Nom de la base de données')
    describe_parser.add_argument('--table', required=True, help='Nom de la table à décrire')

    args = parser.parse_args()

    if args.command == 'create':
        create_table(args.db, args.table, args.columns)
    elif args.command == 'import':
        import_excel(args.db, args.table, args.file)
    elif args.command == 'delete':
        delete_table(args.db, args.table)
    elif args.command == 'delete-db':
        delete_db(args.db)
    elif args.command == 'list-tables':
        list_tables(args.db)
    elif args.command == 'view':
        view_table(args.db, args.table)
    elif args.command == 'describe':
        describe_table(args.db, args.table)
    else:
        show_help()

if __name__ == '__main__':
    main()
