import csv
import matplotlib.pyplot as plt
from datetime import datetime

def calculate_age(date_of_birth):
    return datetime.now().year - datetime.strptime(date_of_birth, '%Y-%m-%d').year

try:
    with open("employees.csv", encoding='utf-8') as file:
        data = list(csv.DictReader(file))
except FileNotFoundError:
    print("Помилка: файл CSV відсутній або пошкоджений.")
    exit()

male_count = sum(1 for row in data if row["Стать"] == "чоловік")
female_count = sum(1 for row in data if row["Стать"] == "жінка")

categories = {"<18": 0, "18-45": 0, "45-70": 0, "70>": 0}
gender_categories = {key: {"чоловік": 0, "жінка": 0} for key in categories}

for row in data:
    age = calculate_age(row["Дата народження"])
    if age < 18:
        category = "<18"
    elif 18 <= age <= 45:
        category = "18-45"
    elif 46 <= age <= 70:
        category = "45-70"
    else:
        category = "70>"

    categories[category] += 1
    gender_categories[category][row["Стать"]] += 1

print(f"Чоловіків: {male_count}, Жінок: {female_count}")
plt.bar(["чоловіки", "жінки"], [male_count, female_count])
plt.title("Кількість співробітників за статтю")
plt.show()

for category, count in categories.items():
    print(f"{category}: {count}")
    plt.bar(["чоловіки", "жінки"], [gender_categories[category]["чоловік"], gender_categories[category]["жінка"]])
    plt.title(f"Кількість співробітників у категорії {category}")
    plt.show()
