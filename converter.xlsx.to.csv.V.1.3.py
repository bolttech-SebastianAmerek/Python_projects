import os
import pandas as pd
import datetime

# Ścieżki bazowe
input_base_path = r"C:\Users\sebastian.amerek\OneDrive - Digital Care\Shared Documents - DCSA\General\DCSA Reports (H)\Pay@"
output_full_base_path = r"C:\Users\sebastian.amerek\OneDrive - Digital Care\Shared Documents - DCSA\General\DCSA Reports (H)\Pay@\FULL\Upload Files"
output_partial_base_path = r"C:\Users\sebastian.amerek\OneDrive - Digital Care\Shared Documents - DCSA\General\DCSA Reports (H)\Pay@\PARTIAL\Upload Files"


# Pliki wejściowe i ustawienia
input_file = "Create new Pay@ file.xlsx"
prefix = "11529"

# Obliczenie numeru sekwencyjnego
full_existing_files = [f for f in os.listdir(output_full_base_path) if f.startswith(f"ACCOUNT_{prefix}_")]
partial_existing_files = [f for f in os.listdir(output_partial_base_path) if f.startswith(f"ACCOUNT_{prefix}_")]
existing_files = full_existing_files + partial_existing_files
#existing_files = [f for f in os.listdir(output_base_path) if f.startswith(f"ACCOUNT_{prefix}_")]
if existing_files:
    seq_nos = [int(f.split("_")[2]) for f in existing_files]
    next_seq_no = max(seq_nos) + 1
    seq_no = f"{next_seq_no:06d}"
else:
    seq_no = "000001"

date = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
output_file = f"ACCOUNT_{prefix}_{seq_no}_{date}.csv"
input_path = os.path.join(input_base_path, input_file)

# Sprawdzenie wartości w komórce B3 arkusza "FULLorPartial"
b3_value = pd.read_excel(input_path, sheet_name="FULLorPartial", usecols="B", nrows=3).iloc[1, 0]

# Wybór odpowiedniego arkusza na podstawie wartości w B3
if b3_value == "FULL":
    sheet_to_use = "FULL"
    output_base_path = r"C:\Users\sebastian.amerek\OneDrive - Digital Care\Shared Documents - DCSA\General\DCSA Reports (H)\Pay@\FULL\Upload Files"
elif b3_value == "PARTIAL":
    sheet_to_use = "Partial"
    output_base_path = r"C:\Users\sebastian.amerek\OneDrive - Digital Care\Shared Documents - DCSA\General\DCSA Reports (H)\Pay@\PARTIAL\Upload Files"
else:
    raise ValueError("Nieprawidłowa wartość w komórce B3. Oczekiwano 'FULL' lub 'Partial'.")

# Ścieżki pliku
output_path = os.path.join(output_base_path, output_file)

# Wczytanie danych z wybranego arkusza
df = pd.read_excel(input_path, sheet_name=sheet_to_use)

# Zapis danych do pliku CSV
df.to_csv(output_path, index=False, quotechar=' ', escapechar='\\', encoding='utf-8')

print(f"File '{input_file}' was converted to '{output_file}' based on sheet '{sheet_to_use}'.")
