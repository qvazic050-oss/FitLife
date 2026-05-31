# Проект FitLife - MVP версия 1.0
MAX_AGE = 95
MIN_AGE = 18
MAX_WEIGHT = 300
MIN_WEIGHT = 30
MAX_HEIGHT = 2.5
MIN_HEIGHT = 1.0
user_name = input("Как вас зовут? ")
while True:
    try:
        user_age = int(input("Сколько вам лет? "))
        if MIN_AGE <= user_age <= MAX_AGE:
            break
    except ValueError:
        print("Пожалуйста, введите Ваш возраст числом (от 18 до 95 лет).")
while True:
    try:
        user_weight = float(input("Сколько вы весите? "))
        if MIN_WEIGHT <= user_weight <= MAX_WEIGHT:
            break
    except ValueError:
        print("Пожалуйста, введите корректный вес числом (от 30 до 300 кг).")
while True:
    try:
        user_height = float(input("Какой у вас рост? ").replace(",", "."))
        if MIN_HEIGHT <= user_height <= MAX_HEIGHT:
            break
    except ValueError:
        print("Пожалуйста, введите корректный рост числом (от 1.0 до 2.5 м).")
bmi = round(user_weight / (user_height ** 2), 1)
water_liters = round(user_weight * 30 / 1000)
print(f"{user_name}, ваш ИМТ: {bmi:}")
print(f"Норма воды: {water_liters:} литров в день.")
