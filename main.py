import pandas as pd
import os

# Ścieżki do katalogów z danymi
phone_accel_path = 'Dataset/wisdm-dataset/raw/phone/accel'
phone_gyro_path = 'Dataset/wisdm-dataset/raw/phone/gyro'

# Kolumny odpowiadające formatowi danych
columns = ['subject_id', 'activity_code', 'timestamp', 'x', 'y', 'z']

# Funkcja do wczytywania danych z katalogu
def load_data_from_directory(directory_path):
    all_data = []
    for filename in os.listdir(directory_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory_path, filename)
            # Wczytaj plik jako DataFrame
            data = pd.read_csv(file_path, header=None, names=columns, delimiter=',', engine='python')
            # Dodaj dane do listy
            all_data.append(data)
    # Połącz wszystkie pliki w jeden DataFrame
    return pd.concat(all_data, ignore_index=True)

# Wczytaj dane z akcelerometru i żyroskopu
accel_data = load_data_from_directory(phone_accel_path)
gyro_data = load_data_from_directory(phone_gyro_path)

# Opcjonalne wyświetlenie pierwszych wierszy dla weryfikacji
print("Dane z akcelerometru:")
print(accel_data.head())
print("\nDane z żyroskopu:")
print(gyro_data.head())
