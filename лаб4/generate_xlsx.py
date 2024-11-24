import csv
import pandas as pd
from datetime import datetime

def categorize_by_age(date_of_birth):
    age = datetime.now().year - datetime.strptime(date_of_birth, '%Y-%m-%d').year
    if age < 18:
        return "younger_18"
    elif 18 <= age <= 45:
        return "18-45"
    elif 46 <= age <= 70:
        return "45-70"
    else:
        return "older_70"

try:
    data = pd.read_csv("employees.csv")
except FileNotFoundError:
    print("Помилка: файл CSV відсутній або пошкоджений.")
    exit()

categories = {"all": data}
for category in ["younger_18", "18-45", "45-70", "older_70"]:
    categories[category] = data[data["Дата народження"].apply(lambda x: categorize_by_age(x) == category)]

try:
    with pd.ExcelWriter("employees.xlsx", engine="openpyxl") as writer:
        for sheet_name, df in categories.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)
    print("Ok")
except Exception as e:
    print("Помилка створення XLSX файлу:", e)
