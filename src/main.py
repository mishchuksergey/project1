import re

def clear_names(file_name: str) -> list:
    """Функция для очистки имен от лишних символов"""
    new_name_lists = list()
    with open ('data/' + file_name, 'r') as names_file:
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

def russian_names_list(names_list: list) ->list:
    """Фильтрация имен написанных на русском"""
    new_names_list = list()
    for name_item in names_list:
        if is_cyrillic(name_item):
            new_names_list.append(name_item)
    return new_names_list



if __name__ == '__main__':
    cleared_name = clear_names('names.txt')

    print(russian_names_list(cleared_name))

