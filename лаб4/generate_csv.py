import csv
import random
from faker import Faker

fake = Faker(locale='uk_UA')

# Словник по батькові
male_patronymics = ["Олексійович", "Андрійович", "Петрович", "Іванович", "Сергійович", "Володимирович", "Олегович"]
female_patronymics = ["Олексіївна", "Андріївна", "Петрівна", "Іванівна", "Сергіївна", "Володимирівна", "Олегівна"]

# Генерація даних
def generate_employee(gender):
    if gender == "чоловік":
        first_name = fake.first_name_male()
        patronymic = random.choice(male_patronymics)
    else:
        first_name = fake.first_name_female()
        patronymic = random.choice(female_patronymics)

    return {
        "Прізвище": fake.last_name(),
        "Ім’я": first_name,
        "По батькові": patronymic,
        "Стать": gender,
        "Дата народження": fake.date_of_birth(minimum_age=16, maximum_age=85).strftime('%Y-%m-%d'),
        "Посада": fake.job(),
        "Місто проживання": fake.city(),
        "Адреса проживання": fake.address(),
        "Телефон": fake.phone_number(),
        "Email": fake.email(),
    }

def create_csv(filename, num_records=2000):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=[
            "Прізвище", "Ім’я", "По батькові", "Стать", "Дата народження",
            "Посада", "Місто проживання", "Адреса проживання", "Телефон", "Email"
        ])
        writer.writeheader()
        for _ in range(num_records):
            gender = "чоловік" if random.random() < 0.6 else "жінка"
            writer.writerow(generate_employee(gender))

create_csv("employees.csv")
