import pandas as pd
from datetime import datetime
import os

def kopskaits_viriesu_slidas(izmers):
    if izmers == 35:
        return 2
    elif izmers == 36:
        return 3
    elif izmers == 37:
        return 4
    elif izmers == 38:
        return 4
    elif izmers == 39:
        return 4
    elif izmers == 40:
        return 5
    elif izmers == 41:
        return 5
    elif izmers == 42:
        return 6
    elif izmers == 43:
        return 7
    elif izmers == 44:
        return 8
    elif izmers == 45:
        return 7
    elif izmers == 46:
        return 6
    elif izmers == 47:
        return 4
    elif izmers == 48:
        return 3
    else:
        return 0

def kopskaits_sieviesu_slidas(izmers):
    if izmers == 32:
        return 2
    elif izmers == 33:
        return 3
    elif izmers == 34:
        return 4
    elif izmers == 35:
        return 5
    elif izmers == 36:
        return 6
    elif izmers == 37:
        return 7
    elif izmers == 38:
        return 7
    elif izmers == 39:
        return 8
    elif izmers == 40:
        return 5
    elif izmers == 41:
        return 3
    elif izmers == 42:
        return 2
    else:
        return 0
def available_and_taken_skates(data, gender, size, date):
    filtered_data = data[(data['Dzimums'] == gender) & (data['Kājas izmērs'] == size) & (data['Nomas datums'] == date)]

    total_count = kopskaits_viriesu_slidas(size) if gender == 'Vīrietis' else kopskaits_sieviesu_slidas(size)
    taken_count = filtered_data.shape[0]
    available_count = total_count - taken_count

    return available_count, taken_count

script_directory = os.path.dirname(os.path.realpath(__file__))

file_path = os.path.join(script_directory, 'nomas dati py.xlsx')

data = pd.read_excel(file_path)

gender_input = input("Ievadiet dzimumu (Vīrietis or Sieviete): ")
size_input = int(input("Ievadiet slidu izmēru: "))
date_input = input("Ievadiet datumu (format: DD.MM.YYYY.): ")

try:
    datetime.strptime(date_input, "%d.%m.%Y.") 
except ValueError:
    print("Nepareizs datuma formāts. Lūdzu ievadīt DD.MM.YYYY.")
    exit()

available, taken = available_and_taken_skates(data, gender_input, size_input, date_input)

print(f"\nPieejamās slidas dzimumam {gender_input}, izmērs {size_input}, šajā datumā {date_input}: {available}")
print(f"Paņemtās slidas dzimumam {gender_input}, izmērs {size_input}, šajā datumā {date_input}: {taken}")