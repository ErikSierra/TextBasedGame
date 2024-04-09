# Project 2
# Erik Sierra
# IT140
# 12/11/22
#

import os
from colorama import Fore, Style, init

init()  # Initialize colorama


def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

rooms = {
    'Lobby': {'South': 'Dining room', 'North': 'Rest area', 'East': 'Laundry Room', 'West': 'Kitchen', 'item': ''},
    'Dining room': {'North': 'Lobby', 'East': 'Bathroom', "item": 'Poke 4'},
    'Bathroom': {'West': 'Dining room', 'item': 'Poke 5'},
    'Laundry Room': {'West': 'Lobby', 'North': 'Gym', 'item': 'Poke 6'},
    'Kitchen': {'East': 'Lobby', 'item': 'Poke 3'},
    'Rest area': {'South': 'Lobby', 'East': 'Storage', 'item': 'Poke 2'},
    'Storage': {'West': 'Rest area', 'item': 'Poke 1'},
    'Gym': {'South': 'Laundry Room', 'item': 'Gym leader'}  # villain
}
# assign variables
items = ['Poke 1', 'Poke 2', 'Poke 3', 'Poke 4', 'Poke 5', 'Poke 6']
item_youSee = ''
inventory = []
inventory_blank = []
Valid_moves = ['North', 'East', 'South', 'West']  # Valid moves are presented in list
location = 'Lobby'
x = 0
move_entered = ''
inventory1 = []


# create function to print objective
def objective():  # Function to print story
    print(Fore.GREEN +
        "--------------------------------------------------------------------------------------------------------------------------- \nYou are a Pokémon trainer and accidentally let your Pokémon run away in the "
        "stadium. You need to find and collect your Pokémon in the rooms of the stadium to be able to beat the gym "
        "leader.\nYou won’t be strong enough to beat the gym leader if you don’t have all 6 of your Pokémon. Good "
        "luck! \n "
        "--------------------------------------------------------------------------------------------------------------------------")


# create function to create instructions
def instructions():  # Function to print directions
    print(Fore.CYAN + "You can move: North, East, South, West\n --------------------------------------------------------")


# create function to add items to inventory
def add2_inventory():
    global inventory, inventory1
    get_item = input("Do you want to pick up this item? (Yes or No) ").strip().lower()  # Convert input to lowercase for consistency
    if get_item == "yes":  # Corrected condition
        inventory.append(item_youSee)
        print("   You picked up ", item_youSee)
    elif get_item == 'no':
        print('   You did not pick anything up')
    else:
        print("! ! ! ! INVALID MOVE ! ! ! ! ")


# creates function to move between rooms
def move_room():
    global location, item_youSee, x
    while move_entered != 'Exit':
        clear_screen()
        print(Fore.BLACK + "***********************   NOW IN " + location.upper() + "   *****************************")
        print("   Current Inventory: ", inventory)

        # Convert possible moves to uppercase for comparison
        possible_moves = [direction.upper() for direction in rooms[location] if direction != 'item']

        print("   You can move: ", ', '.join(possible_moves))  # Display possible moves in uppercase
        direction = input("Which direction do you want to move? ").strip().upper()  # Convert input to uppercase

        if direction == 'EXIT':
            print("Boooo, you quit :( Thanks for playing tho!")
            break

        elif direction in possible_moves:
            print("   You moved: ", direction.capitalize())
            new_location = rooms[location][direction.capitalize()].split()
            location = ' '.join(new_location)

            if rooms[location].__getitem__('item') in items: # if statement to determine if "add2_inventory" function runs to add items to player inventory
                item_youSee = rooms[location].__getitem__('item')
                if item_youSee in inventory:
                    Item_seeninInventory = 'Yes'
                else:
                    Item_seeninInventory = 'No'
                if Item_seeninInventory == 'No':
                    print("   You see: ", item_youSee)
                    add2_inventory()  # calls function (above)
                else:
                    print("No items to pick up")
            if len(inventory) == 0:  # if statement to print what is in inventory based on where player is in game
                print("Inventory: No Pokes found yet!")
            else:
                print('Inventory: ', inventory)
            x = 0
            if location == 'Gym':  # If statement: if location is the gym (final room), either player must have length of 6 elements (pokes) in inventory, or they lose (refer to respective print messages)
                if len(inventory) == 6:
                    print('Alright! You defeated the gym leader! You won the Python Gym Badge!')
                    print('Thanks for playing!')
                    break  # breaks while loop
                else:
                    print("Oh no! You didn't find all your pokemon and weren't strong enough to defeat the gym leader")
                    print(
                        "Hope to see you stronger next time!\n--------------------------------------------------------")
                    break  # breaks while loop
        else:  # if player enters invalid direction
            print("That's a wall\n--------------------------------------------------------")
            print("   You can move: ", *possible_moves)
            x = x + 1  # creates if statements to state consequences of too many incorrect inputs (ends game if => 5)
            if x == 4:
                print("You've attempted too many wrong directions. Only 1 more try before the game ends")
            if x > 4:
                print("Game Over. You took too many tries. Read the directions for how to "
                      "move\n--------------------------------------------------------")
                break  # breaks while loop


objective()  # prints story by calling function
instructions()  # Prints directions by calling function
move_room()  # Calls function to move between rooms
