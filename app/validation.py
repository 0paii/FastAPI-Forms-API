import re
from datetime import datetime


def check_date(value: str) -> bool:
    """Проверка строки на соответствие формату даты

    Поддерживаемые форматы:
    - "%Y-%m-%d"
    - "%d.%m.%Y"
    """
    def parse_date(date_str: str) -> bool:
        try:
            datetime.strptime(value, date_str)
            return True
        except ValueError:
            return False

    return parse_date("%Y-%m-%d") or parse_date("%d.%m.%Y")


TYPE_VALIDATORS = {
    "date": check_date,
    "tel": lambda value: re.fullmatch(r"((8|\+7)[\- ]?)(\(?\d{3}\)?[\- ]?)?[\d\- ]{10}", value),
    "email": lambda value: re.match(r"[^@]+@[^@]+\.[^@]+", value),
    "str": lambda value: True
}


def template_validation(template: dict, form_data: dict) -> int:
    """
    Проверяет, соответствует ли форма шаблону.

    :param template: словарь с описанием шаблона
    :param form_data: словарь с данными, полученными из формы
    :return: количество полей, которые соответствуют шаблону
    """
    for key, value in template.items():
        if key in ['_id', 'name']:
            continue
        if key in form_data.keys() and validate_field(form_data[key], value):
            continue
        return 0
    return len(template)


def validate_field(field_value: str, field_type: str) -> bool:
    """
    Проверяет, соответствует ли значение поля типу поля.

    :param field_value: значение поля
    :param field_type: тип поля
    :return: True, если значение поля соответствует типу, False - в противном случае
    """
    if field_type not in TYPE_VALIDATORS:
        raise ValueError(f"Неизвестный тип поля: {field_type}")
    return bool(TYPE_VALIDATORS[field_type](field_value))
