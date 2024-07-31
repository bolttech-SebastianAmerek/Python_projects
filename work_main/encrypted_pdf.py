import os
import openpyxl
from PyPDF2 import PdfReader, PdfWriter

# Ścieżka do pliku Excel
excel_path = r'.xlsx'

# Ścieżka do folderu z dokumentami
documents_folder = r''
documents_final_folde = r''

# Wczytanie danych z Excela
wb = openpyxl.load_workbook(excel_path)
sheet = wb.active

# Iteracja przez wiersze w pliku Excel
for row in sheet.iter_rows(min_row=2, values_only=True):
    pdf_name = row[0]
    password = row[1]
    
    pdf_path = os.path.join(documents_folder, F"{pdf_name}.pdf")
    
    if os.path.exists(pdf_path):
        # Odczytanie istniejącego PDF-a
        reader = PdfReader(pdf_path)
        writer = PdfWriter()
        
        # Dodanie stron do nowego dokumentu
        for page_num in range(len(reader.pages)):
            writer.add_page(reader.pages[page_num])
        
        # Ustawienie hasła
        writer.encrypt(password)
        
        # Zapisanie zaszyfrowanego PDF-a
        encrypted_pdf_path = os.path.join(documents_final_folde, f'{pdf_name}.pdf')
        with open(encrypted_pdf_path, 'wb') as f:
            writer.write(f)
        
        print(f'Zaszyfrowano: {pdf_name}')
    else:
        print(f'Plik nie znaleziony: {pdf_name}')