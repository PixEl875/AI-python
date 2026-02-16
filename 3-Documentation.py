# Нaпиши документацию (docstring) для этой функции на русском языке в формате Google Style
# Укажи:
# - Что делает функция (1 предложение)
# - Назначение каждого параметра (attack, defense, level)
# - Что возвращает
# - Пример использования с числами

# Исправлено ИИ

def calculate_damage(attack, defense, level):
    """
    Вычисляет итоговый урон на основе параметров атаки, защиты и уровня.

    Args:
        attack (float): Значение атаки персонажа.
        defense (float): Значение защиты персонажа.
        level (int): Уровень персонажа.

    Returns:
        int: Итоговый урон (округленный до целого).

    Example:
        damage = calculate_damage(10, 5, 3)
        # В этом случае результат будет равен 10*1.5 - 5*0.3 + 3*2 = 15 - 1.5 + 6 = 19.5,
        # итоговый урон после преобразования в целое: 19
    """
    base = attack * 1.5
    reduction = defense * 0.3
    bonus = level * 2
    final = base - reduction + bonus
    if final < 1:
        final = 1
    return int(final)


