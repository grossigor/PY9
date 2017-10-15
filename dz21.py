def read_cookbook_from_file(filename, code):
	cookbook = {}
	with open(filename, encoding=code) as f:
		for line in f:
			ing_count = int(f.readline())
			ingridients = []
			for i in range(ing_count):
				ingridient = f.readline().strip().split('|')
				ingridients.append({'ingridient_name' : ingridient[0], 'quantity' : int(ingridient[1]), 'measure': ingridient[2]})
			cookbook[line.strip()] = ingridients
	return cookbook

def get_shop_list_by_dishes(cook_book, dishes, person_count):
	shop_list = {}
	for dish in dishes:
		for ingridient in cook_book[dish]:
			new_shop_list_item = dict(ingridient)
			new_shop_list_item['quantity'] *= person_count
			if new_shop_list_item['ingridient_name'] not in shop_list:
				shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
			else:
				shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
	return shop_list

def print_shop_list(shop_list):
	for shop_list_item in shop_list.values():
		print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], shop_list_item['measure']))

def create_shop_list():
	person_count = int(input('Введите количество человек: '))
	dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
	cookbook = read_cookbook_from_file('cookbook.txt','utf-8')
	shop_list = get_shop_list_by_dishes(cookbook, dishes, person_count)
	print_shop_list(shop_list)

create_shop_list()