def get_file_text(filename, encoding):
	import chardet
	with open(filename, encoding=encoding) as f:
		data = f.read()
		return data

def get_json_data(filename, encoding):
	import json
	with open(filename, encoding=encoding) as f:
		data = json.load(f)
		return data

def get_file_encoding(filename):
	import chardet
	with open(filename, 'rb') as f:
		data = f.read()
		result = chardet.detect(data)
		return result['encoding']

def parse_json_data(json_data):
	data = ''
	for i in range(len(json_data['rss']['channel']['items'])):
		data += json_data['rss']['channel']['items'][i]['description'] + ' '
	return data

def convert_text_to_list(text):
	wordlist = text.strip().lower().split(' ')
	return wordlist


def get_words_count(wordlist):
	words_count = {}
	for word in wordlist:
		if len(word) >= 6:
			if word in words_count:
				words_count[word] += 1
			else:
				words_count[word] = 1
	words_count = sorted(words_count.items(), key=lambda item: item[1], reverse = True) 
	return words_count

def get_top10(words_count):
	top10 = {}
	for word_count in words_count:
		word, count = word_count
		if count not in top10:
			top10[count] = word
		else:
			top10[count] += ', ' + word
		if len(top10) == 10:
			break
	return top10

def print_top10(filename, top10):
	print('Наиболее упоминаемые слова в файле {}:'.format(filename))
	for count, word in top10.items():
		print('Слово {} упомянуто {} раз'.format(word, count))

def main():
	while True:
		print('Введите имя файла для подсчёта:')
		filename = input()
		if '.txt' in filename:
			encoding = get_file_encoding(filename)
			data = get_file_text(filename, encoding)
		elif '.json' in filename:
			encoding = get_file_encoding(filename)
			text = get_json_data(filename, encoding)
			data = parse_json_data(text)
		else:
			print('Неподдерживаемое расширение файла, попробуйте еще раз.')
			continue
		wordlist = convert_text_to_list(data)
		words_count= get_words_count(wordlist)
		top_list = get_top10(words_count)
		print_top10(filename, top_list)

main()