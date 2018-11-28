# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))


def search_in_file(files_sql):
    while len(files_sql) > 1:
        search_str = str.lower(input('Введите строку для поиска: '))
        result = []
        for file in files_sql:
            file_path = os.path.join(migrations, file)
            with open(file_path, encoding='utf-8') as f:
                file_inner = str.lower(f.read())
            if search_str in file_inner:
                result.append(file)
        print('\n'.join(result))
        print('Всего:', len(result))
        files_sql = result


if __name__ == '__main__':
    # ваша логика

    # найти все файлы в директории
    files_all = os.listdir(os.path.join(current_dir, migrations))

    # выбрать только .sql
    files_sql = []
    for file in files_all:
        if '.sql' in file:
            files_sql.append(file)

    search_in_file(files_sql)

    pass