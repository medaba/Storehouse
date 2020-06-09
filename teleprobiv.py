# Получение открытой информации о номере телефона.


import requests
import string
from pprint import pprint


def edit_string(proc_string):
	"""
	Принимает строку и удаляет из нее
	все знаки препинания, символы и пробелы.
	"""
	symbols = string.punctuation + " "
	for symbol in symbols:
		proc_string = proc_string.replace(symbol, "")
	return proc_string


def phone_number(number):
	"""
	Принимает номер телефона (мобильный или стационар)
	Возвращает json объект с информацией по этому номеру.
	"""
	try:
		number = str(number)
		number = edit_string(number)  # Удаление из номера символов и пробелов.
		r = requests.get(
			f'https://htmlweb.ru/geo/api.php?json&telcod={number}'
			)
		return r.json()
	except Exception as e:
		print(e)
		return "Номер не найден"


if __name__ == '__main__':
	# info = phone_number('79510932323')
	info = phone_number('+79994995750')
	pprint(info)
