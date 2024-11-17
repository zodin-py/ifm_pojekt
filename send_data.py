import pandas as pd
import mysql.connector
from mysql.connector import Error

# Verbindung zur MySQL-Datenbank herstellen
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",          # Ersetze mit deinem Host (z. B. 127.0.0.1)
            user="root",               # Dein MySQL-Benutzername
            password="root",       # Dein MySQL-Passwort
            database="zidan",      # Name der Datenbank (erstelle diese vorher oder lass das Skript es tun)
            port=3333  # Dein MySQL-Passwort
        )
        if connection.is_connected():
            print('Erfolgreich mit der MySQL-Datenbank verbunden')
            return connection
    except Error as e:
        print(f'Fehler bei der Verbindung: {e}')
        return None

# CSV-Datei einlesen
def read_csv(file_path):
    return pd.read_csv(file_path, delimiter=';')

# Daten in die MySQL-Datenbank einfügen
def insert_data_to_mysql(df):
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()

        # Tabelle erstellen (falls sie noch nicht existiert)
        create_table_query = """
        CREATE TABLE IF NOT EXISTS Maschinen_Daten (
            id INT AUTO_INCREMENT PRIMARY KEY,
            machine VARCHAR(10),
            job INT,
            start DATETIME,
            end DATETIME
        );
        """
        cursor.execute(create_table_query)
        
        # Einfügen der Daten
        insert_query = """
        INSERT INTO Maschinen_Daten (machine, job, start, end)
        VALUES (%s, %s, %s, %s);
        """
        
        for index, row in df.iterrows():
            cursor.execute(insert_query, (row['machine'], row['job'], row['start'], row['end']))
        
        # Änderungen speichern
        connection.commit()
        print(f'{len(df)} Datensätze wurden eingefügt.')
        
        cursor.close()
        connection.close()

# CSV-Datei einlesen und in die Datenbank einfügen
file_path = 'aktualisierte_datei.csv'  # Ersetze dies mit dem tatsächlichen Pfad zur CSV-Datei
df = read_csv(file_path)
insert_data_to_mysql(df)
