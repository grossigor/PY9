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

def generate_abs_path_migrations(): 
	# Генерируем абсолютный путь до папки с миграциями (Задание №2)
	migrations = 'Migrations'
	current_dir = os.path.dirname(os.path.abspath(__file__))
	abs_path_migrations = os.path.join(current_dir, migrations)
	return abs_path_migrations

def get_sql_files_in_folder(folder_path):
	# Получаем из папки только файлы .sql в виде списка
	files = os.listdir(folder_path)
	sql_files = list(filter(lambda x: x.endswith('.sql'), files))
	return sql_files

def search_string_in_files(search_string, filelist, folder_path):
	result_filelist=[]
	for file in filelist:
		with open(os.path.join(folder_path,file)) as f:
			text = f.read()
			if search_string in text:
				result_filelist.append(file)
				print(file)
	return result_filelist

if __name__ == '__main__':
	folder_path = generate_abs_path_migrations()
	files = get_sql_files_in_folder(folder_path)
	while True:
		search_string = input('Введите строку:	')
		files = search_string_in_files(search_string, files, folder_path)
		print('Всего: {}'.format(len(files)))