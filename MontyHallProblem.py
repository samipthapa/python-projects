#-------Global Variables--------

#Imports the random module
import random

doors = ["A", "B", "C"]

#Answer provided by the player
answer = ""
#Randomly selects the door with the car
car = random.choice(doors)


#Displays the three doors on the screen
def display_doors():
    print("|{0[0]}|\t|{0[1]}|\t|{0[2]}| \n".format(doors))


#Executes the game
def play_game():
    display_doors()
    handle_turns()
    empty_door()
    switch_door()


#Asks user for their answer and determines if the answer is valid
def handle_turns():
    global answer
    answer = input("Choose a door: ")
    answer = answer.upper()

    #Makes sure the answer is valid
    while answer not in ["A", "B", "C"]:
        answer = input("Invalid answer. Choose a door: ")
        answer = answer.upper()

        #Breaks out of loop in case of a valid answer
        if answer in ["A", "B", "C"]:
            break


#Provides a door without the car to the user
def empty_door():

    #In case the answer and the car are behind the same door
    if answer!=car:
        for element in doors:
            if element!=car and element!=answer:
                 print('Door {0} is empty'.format(element))

    else:
        for element in doors:
            #Searches for an empty door
            if element!=car:
                #Breaks out of loop if an empty door is found
                print('Door {0} is empty'.format(element))
                break


#Allows the user to change their final answers
def switch_door():
    switch = input("Would you like to switch door? (Y/N): ")
    switch = switch.upper()

    #Makes sure the input is valid
    while switch not in ["Y", "N"]:
        switch = input("Invalid answer. Choose: (Y/N) ")
        switch = switch.upper()
        if switch in ["Y", "N"]:
            break

    if answer == car:
        if switch == "N":
            print('Congratulations!! You have won the car')
        else:
            print('The car was in Door {0}'.format(car))
    else:
        if switch == "Y":
            print('Congratulations!! You have won the car')
        else:
            print('The car was in Door {0}'.format(car))


#Starts the game
play_game()