import pandas as pd
from datetime import datetime, timedelta

# Funktion zum Auffüllen fehlender Endzeiten
def fill_missing_end_times(data):
    for i in range(len(data)):
        if pd.isna(data.loc[i, 'end']) or data.loc[i, 'end'] == '-':  # Fehlende Endzeiten prüfen
            startzeit_wert = data.loc[i, 'start']
            if isinstance(startzeit_wert, str) and startzeit_wert != '-':  # Sicherstellen, dass Startzeit gültig ist
                startzeit = datetime.strptime(startzeit_wert, '%Y-%m-%d-%H-%M')
                berechnete_endzeit = startzeit + timedelta(hours=1, minutes=5)  # 1 Stunde und 5 Minuten hinzufügen
                data.loc[i, 'end'] = berechnete_endzeit.strftime('%Y-%m-%d-%H-%M')
    return data

# Funktion zum Ersetzen von "-" durch ":"
def replace_time_format(time_string):
    if isinstance(time_string, str):  
        return time_string.replace('-', ':')
    return time_string


def process_csv(file_path, output_path):
    # CSV-Datei einlesen ohne Header
    data = pd.read_csv(file_path, sep=';', header=None, names=['Machine', 'ID', 'start', 'end'])

    # Fehlende Endzeiten auffüllen
    data = fill_missing_end_times(data)

    # Nur die Zeitspalten bearbeiten (start und end), nicht 'Machine'
    data['start'] = data['start'].apply(replace_time_format)
    data['end'] = data['end'].apply(replace_time_format)

    # Nur die Daten speichern
    data.to_csv(output_path, sep=';', index=False, header=False)
    print(f"Die Datei wurde aktualisiert und hier gespeichert: {output_path}")

# Dateipfade definieren
input_file = 'plan_Kopie.csv'  
output_file = 'clean_data.csv' 

# Verarbeitung starten
process_csv(input_file, output_file)
