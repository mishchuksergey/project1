def clear_names(file_name: str) -> list:
    """Функция для очистки имен от лишних символов"""
    new_name_lists = list()
    with open ('date/' + file_name) as names_file:
        names_list = names_file.read().split()
        for name_item in names_list:
            new_name = ''
            for simbol in name_item:
                if simbol.isalpha():
                    new_name += simbol
            if new_name.isalpha():
                new_name_lists.append(new_name)
    return new_name_lists


if __name__ == '__main__':
    cleared_name = clear_names('names.txt')

    for i in cleared_name:
        print(i)
