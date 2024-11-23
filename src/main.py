import re

def clear_names(file_name: str) -> list:
    """Функция для очистки имен от лишних символов"""
    new_name_lists = list()
    with open ('data/' + file_name, 'r', encoding="utf-8") as names_file:
        names_list = names_file.read().split()
        for name_item in names_list:
            new_name = ''
            for simbol in name_item:
                if simbol.isalpha():
                    new_name += simbol
            if new_name.isalpha():
                new_name_lists.append(new_name)
    return new_name_lists


def is_cyrillic(name_item: str) -> bool:
    """Проверка на вхождение кирилицы в строку"""

    return bool(re.search('[а-яА-Я]', name_item))

def filter_russian_names(names_list: list) ->list:
    """Фильтрация имен написанных на русском"""
    new_names_list = list()
    for name_item in names_list:
        if is_cyrillic(name_item):
            new_names_list.append(name_item)
    return new_names_list


def filter_english_names(names_list: list) ->list:
    """Фильтрация имен написанных на английском"""
    new_names_list = list()
    for name_item in names_list:
        if not is_cyrillic(name_item):
            new_names_list.append(name_item)
    return new_names_list


def save_to_file(file_name: str, data: str ) -> None:
    """"Сохраняет данные в файл"""

    with open('data/' + file_name, 'w', encoding="utf-8") as names_file:
        names_file.write(data)


if __name__ == '__main__':
    cleared_name = clear_names('names.txt')

    filtred_names = filter_russian_names(cleared_name)
    save_to_file(
        'russian_names.txt',
        '\n'.join(filtred_names))

    filtred_names = filter_english_names(cleared_name)
    save_to_file(
        'english_names.txt',
        '\n'.join(filtred_names))
