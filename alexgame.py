#author alex apshago january 15 2023
#v1.1
#setup clear screen for multiple systems

# set debug to 1 to enable debugging - in code place if debug == 1: in front of your debug functions
debug=0

global currentloc_x 
currentloc_x = int(50)
global currentloc_y 
currentloc_y = int(50) 

from os import system, name
from time import sleep
from room import Location
from Player import Player

def clear():
	if name =='nt':
		_ = system('cls')
	else:
		_ = system('clear')

def startingscreen():
	gamemode=input('Please choose your path: If Peaceful, type 1 and if Non-peaceful type 2. ')
	if gamemode=='1':
	 	peacefulgame()
	elif gamemode=='2':
		print('This gamemode is still in the works! Please wait patiently.')
		quit() 
	else:
		print('This is not a viable answer. Please retry!')
		sleep(3)
		startingscreen()

def createplayer():
	player = Player(username, 50,50,0,["Shovel","Axe"])
	# print(f"You are starting with {player.starting_dabloon} dabloons. ")
	return(player)

def controls():
	global currentloc_y
	global currentloc_x
	currentroommove = str("location" + str(currentloc_x) + str(currentloc_y) + ".move")
	currentroomtakedabloon = str("location" + str(currentloc_x) + str(currentloc_y) + ".takedabloon")
	currentroomdescribe = str("location" + str(currentloc_x) + str(currentloc_y) + ".decribe")
	currentroomdebloons = eval(str("location" + str(currentloc_x) + str(currentloc_y) + ".starting_dabloon"))
	currentroomdig = str("location" + str(currentloc_x) + str(currentloc_y) + ".dig")

	print("")
	print(eval(currentroomdescribe))
	print(f"This room has {currentroomdebloons} dabloons in it.")
	if debug == 1:print(f"debug: {currentloc_x, currentloc_y}")
	control=input('? ')
	control=control.lower()

	if control=="inventory":
	 	print(f"Current debloon amount is {player.starting_dabloon}. ") 
	 	print("")
	 	print(f"Your current items are:")
	 	print(*player.bag,sep='\n')
	 	controls()
	elif control == 'map':
		print(f'Current location is {currentloc_x, currentloc_y}.')
		showmap()
		controls()
	elif control == "up": 
		newcurrentloc_y = eval(currentroommove)('N', currentloc_y) 
		currentloc_y = newcurrentloc_y
		controls()
	elif control == "down": 
		newcurrentloc_y = eval(currentroommove)('S', currentloc_y) 
		currentloc_y = newcurrentloc_y
		controls()	
	elif control == "left": 
		newcurrentloc_x = eval(currentroommove)('E', currentloc_x) 
		currentloc_x = newcurrentloc_x
		controls()	
	elif control == "right": 
		newcurrentloc_x = eval(currentroommove)('W', currentloc_x) 
		currentloc_x = newcurrentloc_x
		controls()		
	elif control=='take dabloon':
		dabloonstoadd = eval(currentroomtakedabloon)(1)
		player.adddabloon(dabloonstoadd)
		controls()
	elif control=='dig':
		prize = eval(currentroomdig)()
		player.addprize(prize)
		controls()

	elif control=='help':
		print("")
		print("Commonly used commands")
		print("'Inventory' - shows you your items bought and dablooons found") 
		print("'Map' -  a map that gives you your x and y coordinates")
		print("'Take Dabloon' - picks up or recieves dabloons gived")
		print("'Give Dabloon' - gives dabloon away to buy items")
		print("'Up' - moves player up") 
		print("'Down' -  moves player down")
		print("'Left' - moves player left")
		print("'Right' - moves player right")	
		print("'Dig' - dig for something")
		print("'Help' - shows player list of commands")
		controls()
	
	elif control=='give dabloon':
		player.takedabloon(10)
		controls()
	
	else:
		print("")
		print("This is not a valid command!")
		controls()

def peacefulgame():
	print("If you want to learn more about the game controls, please type 'Help'")
	print("---")
	controls()

def showmap():
	print("45 46 47 48 49 50 51 52 53 54 55")
	print("53")
	print("52")
	print("51             []")
	print("50          [] [] []")
	print("49             []")
	print("48             []")
	print("47             []")
	print("46             []")
	print("45")

#all functions defined above this line
clear()
print('Hello user! Welcome to the game.')
username=input('What is your name? ' )
print(f'Welcome {username}.')

#build locations for level 1 (up,down,left,right)
location5050=Location('You are in a large green forest.',0,0,10, 1, 1, 1, 1,"yes","sword")
location4950=Location('You are in a left.',0,0,20, 0, 0, 0, 1,"no",0)
location5150=Location('You are in a right.',0,0,30, 0, 0, 1, 0,"no",0)
location5051=Location('You are in a top.',0,0,40, 0, 1, 0, 0,"no",0)
location5049=Location('You are in a first bottom.',0,0,5, 1, 1, 0, 0,"no",0)
location5048=Location('You are in a second bottom.',0,0,0, 1, 1, 0, 0,"no",0)
location5047=Location('You are in a third bottom.',0,0,0, 1, 1, 0, 0,"no",0)
location5046=Location('You are in a fourth bottom.',0,0,50, 1, 0, 0, 0,"no",0)

player = createplayer()
startingscreen()