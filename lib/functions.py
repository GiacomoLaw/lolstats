import msvcrt as m
import requests


def waitforkey():
	m.getch()


def serverselect():
	url = "https://raw.githubusercontent.com/GiacomoLaw/lolstats/master/lib/serverlist.json"
	data = requests.get(url).json()
	for index, element in enumerate(data, start=1):
		print("{}. {}".format(index, element['richname']))
	server_choice = input("What server do you want? Enter the number. ")
	if server_choice == '1':
		my_region = 'br1'
		print('Server set to Brazil.')
	elif server_choice == '2':
		my_region = 'eun1'
		print('Server set to Europe Nordic and East.')
	elif server_choice == '3':
		my_region = 'euw1'
		print('Server set to Europe West.')
	elif server_choice == '4':
		my_region = 'jp1'
		print('Server set to Japan.')
	elif server_choice == '5':
		my_region = 'kr1'
		print('Server set to Korea.')
	elif server_choice == '6':
		my_region = 'la1'
		print('Server set to Latin America North.')
	elif server_choice == '7':
		my_region = 'la2'
		print('Server set to Latin America South.')
	elif server_choice == '8':
		my_region = 'na'
		print('Server set to North America.')
	elif server_choice == '9':
		my_region = 'oc1'
		print('Server set to Oceania.')
	elif server_choice == '10':
		my_region = 'tr1'
		print('Server set to Turkey.')
	elif server_choice == '11':
		my_region = 'ru'
		print('Server set to Russia.')
	elif server_choice == '12':
		my_region = 'pbe1'
		print('Server set to Public Beta.')
	else:
		print('Error. Select one of the numbers.')


print(serverselect())
