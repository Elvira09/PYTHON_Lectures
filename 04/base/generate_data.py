import uuid
import names
import datetime
import random



def unid():
	un_id = uuid.uuid1()
	return un_id
# print(id())

def generate_name():
	name = names.get_first_name()
	return name
# print(generate_name())

def generate_surname():
	surname = names.get_last_name()
	return surname
# print(generate_surname())

def generate_birthday():
		date_day = random.randint(1, 28)
		date_month = random.randint(1, 12)
		date_year = random.randint(1970, 2000)
		date_random = datetime.date(date_year, date_month, date_day)
		return date_random
# print(generate_birthday())

def generate_phone():
	phone = '+' + str(random.randint(30000000000, 99999999999))
	return phone
# print(generate_phone())

with open('Lectures/04/base/Lect04_basa_data.txt', 'w') as file:
	for i in range(10):
		file.write(f'id: {unid()}\
				name: {generate_name()}\
				surname: {generate_surname()}\
				birthday: {generate_birthday()}\
				phone: {generate_phone()} \n')


with open('Lectures/04/base/Lect04_basa_data.csv', 'w') as file:
	for i in range(10):
		file.write(f'id: {unid()}\
				name: {generate_name()}\
				surname: {generate_surname()}\
				birthday: {generate_birthday()}\
				phone: {generate_phone()} \n')


with open('Lectures/04/base/Lect04_basa_data.csv', 'w') as file:
	for i in range(3):
		file.write(f"id: {unid()} \n"
		"name: {generate_name()}  \n"
		"surname: {generate_surname()} \n"
		"birthday: {generate_birthday()} \n"
		"phone: {generate_phone()} \n\n")