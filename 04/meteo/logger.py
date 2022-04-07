# Модуль 2: логирование

from datetime import datetime as dt


def temperature_logger(data):
	time = dt.now().strftime('%H:%M')
	with open('Lect04_meteo_log.csv', 'a') as  file:
		file.write('{}; temperature; {}\n'.format(time, data))


def pressure_logger(data):
	time = dt.now().strftime('%H:%M')
	with open('Lect04_meteo_log.csv', 'a') as  file:
		file.write('{}; pressure; {}\n'
					.format(time, data))


def wind_speed_logger(data):
	time = dt.now().strftime('%H:%M')
	with open('Lect04_meteo_log.csv', 'a') as  file:
		file.write('{}; wind_speed; {}\n'
					.format(time, data))
		
 