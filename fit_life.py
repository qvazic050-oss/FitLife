# Проект FitLife - MVP версия 1.0
user_name = input("Как вас зовут? ")
user_age = int(input("Сколько вам лет? "))
while True:
    if user_age < 18:
        print("Извините, эта программа предназначена для пользователей старше 18 лет.")
        user_age = int(input("Пожалуйста, введите ваш возраст: "))
    if user_age > 95: 
        print("Извините, эта программа предназначена для пользователей младше 95 лет.")
        user_age = int(input("Пожалуйста, введите ваш возраст: "))      
    else:
        break
user_weight = float(input("Сколько вы весите? ").replace(",", "."))
while True:
    if user_weight < 30:
        print("Извините, эта программа предназначена для пользователей с весом не менее 30 кг.")
        user_weight = float(input("Пожалуйста, введите ваш вес: "))
    if user_weight > 150:
        print("Внимание: Вам нужно срочно снизить вес. Обратитесь к врачу.")
        user_weight = float(input("Пожалуйста, введите ваш вес: "))
    else:
        break
user_height = float(input("Какой у вас рост (в метрах)? ").replace(",", "."))
while True:
    if user_height < 1.0:
        print("Извините, эта программа предназначена для пользователей с ростом не менее 1 метра.")
        user_height = float(input("Пожалуйста, введите ваш рост (в метрах): "))
    if user_height > 2.5:
        print("Внимание: Ваш рост необычно высокий. Пожалуйста, проверьте введенные данные.")
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

