#4/10/2018
#John Cruz

import random
import os
import time
import sqlite3

bike_list = []
bike = []
sold_bikes = []

#Make/open .db file to add bike information
bikeDatabase = sqlite3.connect('Bikes.db')
pointer = bikeDatabase.cursor()

### FIXME
''' count all rows (bikes) in the database and return a total.  '''
#selectAll = pointer.execute("""SELECT * FROM bikes """)
#dataBaseSize = len(selectAll.fetchall())


def clear():
	''' clear the shell, no more scrolling. only works out side of idle. kinda buggy in the idle.'''
	os.system('clear')


def wait(seconds = None):
	'''wait(seconds) with the default set to 1 seconds if left blank flaots can be use to get fractions of a secpond '''
	if (seconds == None):
		time.sleep(1)
	else:
		time.sleep(seconds)


def disp2d(array):
	''' displays 2d arrays in a neat table. if array is empty it will print that it is empty'''
	if (len(array) == 0):
		print ('(Empty)\n')
	else:
		for i in range (len(array)): # go through a 2 dimentional array and display a table 
			print(i+1, end=')\t')
			for j in range (len(array[0])):
				print(array[i][j], end='\t')
			print()
		print()


def disp1d(array):
	''' displays 2d arrays in a neat table. if array is empty it will print that it is empty'''
	if (len(array) == 0):
		print ('(Empty)\n')
	else:
		for j in range (len(array[0])): # display 1 dimentioanl Array on a one collum table
			print(array[j])
		print()


def creatSqlTable ():
	'''Creates a table with in the .db file names Bikes future updates will allow to creat any named table with any amount of values '''
	pointer.execute("""CREATE TABLE IF NOT EXISTS bikes (tag TEXT, serialNumber TEXT, model TEXT,  brand TEXT)""")
	bikeDatabase.commit()
	

def addData(tag, serialNumber, model, brand):
	'''adds Data to "bike" table. allow for 4 perameters '''
	pointer.execute("""INSERT INTO bikes (tag, serialNumber, model, brand) VALUES(?, ?, ?, ?) """, (tag, serialNumber, model, brand))
	bikeDatabase.commit()


def addLineData(Array):
	''' allows to add 2d array into bike table '''
	pointer.executemany("""INSERT INTO bikes (tag, serialNumber, model, brand) VALUES(?, ?, ?, ?) """, (Array))
	bikeDatabase.commit()


def displayAllData ():
	'''displays all data with in the bike table ''' 
	for row in pointer.execute('SELECT * FROM bikes'):       	
		print (row)


def grabRow (tag):
	''' allows to select one row with in the bike table '''
	pointer.execute("""SELECT * FROM bikes WHERE tag = (?) """,(tag,))
	for row in pointer.fetchall():       	
		return (row)


def DELETEALL():
	'''USE WITH CATION!!! REMOVES ALL DATA PERMENITLY from Bike Table '''
	pointer.execute("""DELETE FROM bikes""")


def closeAll():
	'''saves all and closes any open 'connection' to the database '''
	bikeDatabase.commit()
	pointer.close()
	bikeDatabase.close()

##################################################################################
'''ALL RANDON FUCTIONS USED FOR AUTO GENERATION OF DATA FOR DEBUGING PORPUSES '''
##################################################################################

def RandomInt ():
	''' generates a 8 digit number and then converted to string data type '''
	randomNumber = random.randint(10000000,99999999)
	return str(randomNumber)


def RandomModel ():
	'''randon gen of models of bikes'''
	randomNumber = random.randint(1,3)
	
	if (randomNumber == 1):
		return ('CHD')

	elif (randomNumber == 2):
		return ('WorkHorse')
		
	elif (randomNumber == 3):
		return ('Mover')


def RandomBrand ():
	'''randon gen of brands of bikes '''
	randomNumber = random.randint(1,3)
	
	if (randomNumber == 1):
		return ('Schwinn')

	elif (randomNumber == 2):
		return ('Summit')
		
	elif (randomNumber == 3):
		return ('Atlas')


def mainMenu():
	clear ()
	print ('''Bike Invetory Logger
1) warehouse
2) sales
3) techinician
4) Master menu
5) To quit''')

	global what_to_do
	what_to_do = int (input ('what to do? '))


def warehouse ():
	clear()
	print('Reciving')
	flag = 'y'
	while (flag == 'y'):

		brand = str(input('Enter the brand of the Bike :'))
		model = str(input(' Enter the model of the Bike :'))
		serialNumber = str(input('Enter the serial number of the Bike :'))
		tag = str(input(' Please asign a tag number to the bike and record it :'))

		addData(tag, serialNumber, model, brand)

		flag = str(input('continue? y/n'))
		clear()

	#print ('Total bike recieved in')
	wait()


def sales ():
	clear()
	# this for loop will run thru bike_list and display to the user a sorted bike list via tag numbers
	displayAllData()
	print('Enter \'sell\' to end invoice')

	x = 'NOT sell'
	while (x != 'sell'):
		x = str (input('Enter a tag Number to add to the invoice : '))					
		sold_bikes.append(grabRow(x))
	
	print ()
	
	for bike in sold_bikes:
		print (bike)
	a = str(input('Press Enter to Continue.'))


def tech ():
	clear()
	if (len(sold_bikes) == 0):
		print ('they are no bikes to be sold')
		wait()

	else:
		print ('\nPlease pull these bikes')
		print ('num	tag	sn	model	brand	\n')
		disp1d(sold_bikes)

		done = str(input('clear?'))
		if (done == 'y'):
			print('bikes cleared')
			del sold_bikes[:]
			print (sold_bikes)


def underDev():
	clear()
	print ('Still under development')
	wait()


##FIXME CLEAN 
def debug():
	''' DEBUG menu use with CATION. can Cause irreversable damage to database '''
	clear()
	outter_flag = 'y'
	while (outter_flag == 'y'):
		clear()
		print('''DEBUG
1) Auto populate - takes a few moments.
2) DELETE bike list
3) DISPLAY all List
4) Set up DATABASE bikes.db
5) Display from database
6) DELETE all in database
7) Grab row
9) To exit''')
		inner_flag = str(input(''))

		if (inner_flag == '1'):
		#for auto populating 10 line items and for debugging
			for i in range(10):	
				bike_list = [(RandomInt(), RandomInt(), RandomModel(), RandomBrand())]
				addLineData(bike_list)
				bike_list = []
			wait()

		elif (inner_flag == '2'):
			del bike_list [:]

		elif (inner_flag == '3'):
			clear()
			print ('\nbike\n')
			disp2d(bike)
			print ('\nbike_list\n')
			disp2d(bike_list)
			print ('\nsold_bikes\n')
			disp2d(sold_bikes)
			wait()	

		elif (inner_flag == '4'):
			clear()
			creatSqlTable()
			print('SQL database with table Created')
			wait()		

		elif (inner_flag == '5'):
			clear()
			displayAllData()
			a = str(input('Press Enter to Continue.'))	

		elif (inner_flag == '6'):
			clear()
			DELETEALL()
			wait()		

		elif (inner_flag == '7'):
			displayAllData()

			x = str (input('tag'))			

			print()			

			sold_bikes.append(grabRow(x))
			print (sold_bikes)

			q = str (input('tag'))

		elif (inner_flag == '9'):
			print ('end')
			wait()
			outter_flag = 'n'


#######################################################################
##############     Main Loop Area    ##################################
#######################################################################


flag = True
while (flag == True):
	mainMenu()

	if (what_to_do == 1):
		warehouse()

	elif (what_to_do == 2):
		sales()

	elif (what_to_do == 3):
		tech()

	elif (what_to_do == 4):
		debug()

	elif (what_to_do == 5):
		closeAll()
		flag = False
		clear()

	else:
		print ('try again')

