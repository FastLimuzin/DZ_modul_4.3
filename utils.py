import re

def get_reg_data():
    """Возвращает паттерны для проверки ввода данных."""
    return [
        r'^[A-Za-zА-Яа-яЁё\s]+$',  # Имя (только буквы и пробелы)
        r'^[A-Za-zА-Яа-яЁё\s]+$',  # Фамилия (только буквы и пробелы)
        r'^\+?[0-9]{10,15}$',       # Телефон (10-15 цифр, возможно с +)
        r'^[\w\.-]+@[\w\.-]+\.\w+$'  # Email
    ]

def check_unique_data(user_data, data_to_check):
    """Проверяет уникальность введенных данных."""
    return user_data not in data_to_check

def reg_check(user_data, reg_pattern, users_list, data_to_check=None):
    """Проверяет введенные данные пользователя."""
    if re.match(reg_pattern, user_data) is None:
        print("Неверный формат данных.")
        return None

    # Проверяем уникальность, если предоставлены данные для проверки
    if data_to_check is not None and not check_unique_data(user_data, data_to_check):
        print("Данные должны быть уникальными.")
        return None

    return user_data