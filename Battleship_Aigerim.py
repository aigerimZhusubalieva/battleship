'''A simplified version of the battleship game. 
User plays against the computer, 
trying to guess where it hid the ship on the board.'''

import random
import os
import time

#Set ship size and board dimensions
SHIP_SIZE = 4		  #minimum 2 and maximum 4
BOARD_DIMENSION = 10  #minimum 4 and maximum 10

#create a board with given dimensions to store ship location
sboard = []

for letter in range(BOARD_DIMENSION):
	number_list = []
	for number in range(BOARD_DIMENSION):
		number_list.append(" ")
	sboard.append(number_list)

#create an empty copy of the board to display
dboard = []

for letter in range(BOARD_DIMENSION):
	number_list = []
	for number in range(BOARD_DIMENSION):
		number_list.append(" ")
	dboard.append(number_list)

#randomly locoate the ship
ship_location_letter = random.randint(0, BOARD_DIMENSION-SHIP_SIZE)
ship_location_number = random.randint(0, BOARD_DIMENSION-SHIP_SIZE)
ship_orientation = random.randint(0,1)		#vertical(0) or horizontal(1)

for n in range(SHIP_SIZE):

	sboard[ship_location_number][ship_location_letter] = "X"

	if ship_orientation == 0:
		ship_location_number += 1
	else:
		ship_location_letter += 1

	
#Start the game
count = 0  #keeps the score
hit = 0    #count of how many times the ship was hit

while not( hit == SHIP_SIZE ):

	#print the board to display for the user
	os.system("clear")
	start_letter = ord("A")
	for letter in range(BOARD_DIMENSION):
		print("  ", chr(start_letter), end="")
		start_letter += 1
	print()  

	for n in range(BOARD_DIMENSION):
		print(" " + "+---"*BOARD_DIMENSION + "+")
		print(n, end="")
		for b in range(BOARD_DIMENSION):
			print("|", str(dboard[n][b]), end = " ")
		print("|")
	print(" " + "+---"*BOARD_DIMENSION + "+")

	#Check user input for lenght, format, case, and range.
	correct_input = False
	start_letter = ord("A")

	while correct_input == False:
		target = input("Enter coordinates in the format A0, B2, C1, etc: ")
		target = list(target)
		if not( len(target) == 2):
			print("Incorrect length, enter again.")
		elif target[0].isalpha() == False or target[1].isdigit() == False:
			print("Incorrect format, enter again.")
		elif ( ord(target[0]) >= (start_letter + BOARD_DIMENSION)) or (int(target[1]) >= BOARD_DIMENSION):
			print("Corrdinates must be within the board range and in upper case, enter again.")
		else:
			correct_input = True 

	#Check if the user hit the ship and update display board accordingly
	target_letter = ord(target[0]) - 65  #convert the ASCII number of the letter to 0-9 format
	target_number = int(target[1])
	
	if dboard[target_number][target_letter] == "X" or dboard[target_number][target_letter] == "#":
		print("You already hit that coordinate, try another one :)")
		time.sleep(1.5) 
	elif sboard[target_number][target_letter] == "X":
		dboard[target_number][target_letter] = "X"
		hit +=1
		count += 1
	else:
		dboard[target_number][target_letter] = "#"
		count += 1

#print the board and score after game is finished
os.system("clear")
start_letter = ord("A")
for letter in range(BOARD_DIMENSION):
	print("  ", chr(start_letter), end="")
	start_letter += 1
print()  

for n in range(BOARD_DIMENSION):
	print(" " + "+---"*BOARD_DIMENSION + "+")
	print(n, end="")
	for b in range(BOARD_DIMENSION):
		print("|", str(dboard[n][b]), end = " ")
	print("|")
print(" " + "+---"*BOARD_DIMENSION + "+")

print("CONGRATULATIONS, YOU WON! :)")
print("YOUR SCORE IS:", count)