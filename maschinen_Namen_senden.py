import pandas as pd
import mysql.connector

# CSV-Datei einlesen mit dem richtigen Separator
csv_file = 'aktualisierte_datei.csv'  # Pfad zur CSV-Datei
df = pd.read_csv(csv_file, sep=';')  # Verwende ';' als Separator

# Entfernen von führenden und nachfolgenden Leerzeichen aus den Spaltennamen
df.columns = df.columns.str.strip()

# Überprüfe die Spaltennamen
print("Spaltennamen:", df.columns)

# Versuche, die Maschinen-Namen zu extrahieren
try:
    machines = df['machine'].unique()  # Einzigartige Maschinen-Namen
except KeyError:
    print("Die Spalte 'machine' wurde nicht gefunden. Bitte überprüfe den Spaltennamen.")
    exit(1)

# Verbindung zur MySQL-Datenbank herstellen
db_connection = mysql.connector.connect(
    host="localhost",          # Ersetze mit deinem Host (z. B. 127.0.0.1)
    user="root",               # Dein MySQL-Benutzername
    password="root",       # Dein MySQL-Passwort
    database="zidan",      # Name der Datenbank (erstelle diese vorher oder lass das Skript es tun)
    port=3333              # der Name deiner Datenbank
)

cursor = db_connection.cursor()

# Erstelle die Tabelle, falls sie nicht existiert
cursor.execute("""
    CREATE TABLE IF NOT EXISTS machines (
        id INT AUTO_INCREMENT PRIMARY KEY,
        machine_name VARCHAR(255)
    );
""")

# Maschinen-Namen in die Datenbank einfügen
for machine in machines:
    cursor.execute("INSERT INTO machines (machine_name) VALUES (%s)", (machine,))

# Änderungen speichern und Verbindung schließen
db_connection.commit()
cursor.close()
db_connection.close()

print("Maschinen-Namen wurden erfolgreich in die Datenbank hochgeladen.")
