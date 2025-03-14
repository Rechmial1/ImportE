import sqlite3
import pytest
import os
import time
import sys

# Ajout du répertoire contenant main.py au chemin Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import import_excel, view_table

# Définition des chemins
TEST_DB = "test_db.sqlite"
TEST_TABLE = "test_table"
TEST_FILE = "tests/people sample.xlsx"

@pytest.fixture(scope="module")
def setup_database():
    # Création d'une base de données et une table de test avant d'exécuter les tests
    conn = sqlite3.connect(TEST_DB)
    cursor = conn.cursor()
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {TEST_TABLE} (matricule TEXT, nom TEXT, prenom TEXT, datedenaissance DATE, status TEXT);")
    conn.commit()
    conn.close()
    
    print("Database created at:", os.path.abspath(TEST_DB))  # Affiche le chemin de la base
    yield
    
def test_import_excel(setup_database):
    # Test de l'importation des données Excel avec mesure du temps d'exécution
    start_time = time.time()
    import_excel(TEST_DB, TEST_TABLE, TEST_FILE)
    end_time = time.time()
    
    conn = sqlite3.connect(TEST_DB)
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {TEST_TABLE};")
    count = cursor.fetchone()[0]
    conn.close()

    assert count > 0, "L'importation a échoué : aucune donnée insérée."
    print(f"Test d'importation réussi. Temps d'exécution : {end_time - start_time:.2f} secondes.")

def test_view_table(setup_database, capsys):
    # Teste l'affichage des données de la table
    view_table(TEST_DB, TEST_TABLE)
    captured = capsys.readouterr()
    
    print("Sortie capturée:", captured.out)  # Débogage : voir la sortie réelle
    assert "Contenu de la table" in captured.out, "L'affichage de la table ne fonctionne pas correctement."
