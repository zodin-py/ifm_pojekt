
import mysql.connector
# Verbindung zur MySQL-Datenbank herstellen
connection = mysql.connector.connect(
    host="localhost",          # Ersetze mit deinem Host (z. B. 127.0.0.1)
    user="root",               # Dein MySQL-Benutzername
    password="root",       # Dein MySQL-Passwort
    database="zidan",      # Name der Datenbank (erstelle diese vorher oder lass das Skript es tun)
    port=3333 # Die Datenbank, mit der du dich verbinden möchtest
)

# Einen Cursor erstellen, um mit der Datenbank zu interagieren
cursor = connection.cursor()

# Abfrage, um alle Tabellen in der Datenbank zu erhalten
cursor.execute("SHOW TABLES")

# Alle Tabellennamen abrufen
tables = cursor.fetchall()

# Alle Tabellen durchlaufen und die Daten aus jeder Tabelle abrufen und drucken
for table in tables:
    table_name = 'machines'
    print(f"Daten aus der Tabelle: {table_name}")
    
    # Abfrage für alle Daten aus der aktuellen Tabelle
    cursor.execute(f"SELECT * FROM {table_name}")
    
    # Alle Ergebnisse abrufen
    rows = cursor.fetchall()
    
    # Jede Zeile drucken
    for row in rows:
        print(row)
    
    print("\n" + "="*50 + "\n")  # Trennlinie zwischen den Tabellen

# Den Cursor und die Verbindung schließen
cursor.close()
connection.close()
