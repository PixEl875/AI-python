# Перепиши этот код калькулятора на Python с соблюдением правил читаемости:
# - Отступы 4 пробела
# - Пробелы вокруг операторов
# - Понятные названия переменных
# - Комментарии для сложных мест
# - Обработка ошибок через try-except

# Исправлено ИИ

try:
    # Ввод первого числа с подсказкой
    first_number = float(input("Введите первое число: "))
    # Ввод второго числа с подсказкой
    second_number = float(input("Введите второе число: "))
    # Ввод операции (+, -, *, /)
    operation = input("Введите операцию (+, -, *, /): ").strip()

    # Выполнение операции по введённому знаку
    if operation == "+":
        result = first_number + second_number
        print("Результат:", result)

    elif operation == "-":
        result = first_number - second_number
        print("Результат:", result)

    elif operation == "*":
        result = first_number * second_number
        print("Результат:", result)

    elif operation == "/":
        # Проверка деления на ноль
        if second_number != 0:
            result = first_number / second_number
            print("Результат:", result)
        else:
            print("Ошибка: деление на ноль!")

    else:
        # Неизвестная операция
        print("Неизвестная операция")

except Exception as e:
    # Обработка непредвиденных ошибок
    print("Произошла ошибка:", e)


