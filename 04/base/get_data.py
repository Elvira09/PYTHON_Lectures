
def get_name():
	with open('Lect04_basa_data.txt', 'r') as file:
		x = 'name'
    	lines = file.read(x).splitlines()
		return lines

print(get_name())