# Проект FitLife - MVP версия 1.0
user_name = input("Как вас зовут? ")
user_age = int(input("Сколько вам лет? "))
while True:
    if user_age < 18:
        print("Ведите корректный возраст")
        user_age = int(input("Пожалуйста, введите ваш возраст: "))
    if user_age > 95:
        print("Ведите корректный возраст")
        user_age = int(input("Пожалуйста, введите ваш возраст: "))
    else:
        break
user_weight = float(input("Сколько вы весите? ").replace(",", "."))
while True:
    if user_weight < 30:
        print("Ведите корректный вес")
        user_weight = float(input("Пожалуйста, введите ваш вес: "))
    if user_weight > 150:
        print("Ведите корректный вес")
        user_weight = float(input("Пожалуйста, введите ваш вес: "))
    else:
        break
user_height = float(input("Какой у вас рост (в метрах)? ").replace(",", "."))
while True:
    if user_height < 1.0:
        print("Ведите корректный рост")
        user_height = float(input("Пожалуйста, введите ваш рост (в метрах): "))
    if user_height > 2.5:
        print("Ведите корректный рост")
        user_height = float(input("Пожалуйста, введите ваш рост (в метрах): "))
    else:
        break
bmi = round(user_weight / (user_height ** 2), 1)
water_ml = round(user_weight * 30)
water_l = water_ml / 1000
print(f"Отчет для пользователя: {user_name} ({user_age} лет)")
print(f"Ваш ИМТ: {bmi}")
print(f"Рекомендуемая норма воды в день: {water_l} л")
print("Расчет окончен. Будьте здоровы!")
