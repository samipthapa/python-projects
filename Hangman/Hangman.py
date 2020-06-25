import random
from word import words
#-------Global Variables--------

#The word which has to be guessed by the player
secret_word = ''

#Creates the dashed word
blank = []

#Counts the remaining number of chances (appendages)
counter = 0

#For verifying guesses
alphabet = 'QWERTYUIOPLKJHGFDSAZXCVBNM'


#Generates the word from a list
def word_generator():
    global secret_word
    secret_word = random.choice(words)
    secret_word = secret_word.upper()


#Executes the game of hangman
def play_game():
    word_generator()
    hints()

    #Loops until the user guessses the right answer or run out of tries
    while counter<=5 and (''.join(blank))!=secret_word:
        drawing()
        checks_the_guess()

    #Checks if the player won
    if (''.join(blank)) == secret_word:
        print('Congratulations. You got the word right\n')

    #Checks if the player lost
    else:
        drawing()
        print(f'Sorry you ran out of tries. The word was {secret_word}')
    play_again()


#Provides hint to the user
def hints():
    global blank
    blank = []
    print("\nLet's Play Hangman")
    for i in range(len(secret_word)):
        blank.append('_')

    #Assigns the random hint to the player
    value = random.choices(secret_word, k = 2)
    for i in range(len(secret_word)):
        if secret_word[i] == value[0]:
            blank[i] = value[0]
        elif secret_word[i] == value[1]:
            blank[i] = value[1]


#Prints the picture of hangman in accordance with the player's remaining appendages
def drawing():
    if counter == 0:
        print('\n _______\n |     |\n |')
    elif counter == 1:
        print(' _______\n |     |\n |     O')
    elif counter == 2:
        print(' _______\n |     |\n |     O\n |     |')
    elif counter == 3:
        print(' _______\n |     |\n |     O\n |    /|')
    elif counter==4:
        print(' _______\n |     |\n |     O\n |    /|\\')
    elif counter == 5:
        print(' _______\n |     |\n |     O\n |    /|\\\n |    /')
    elif counter == 6:
        print(' _______\n |     |\n |     O\n |    /|\\\n |    / \\')

    print(f"\n{''.join(blank)}\n")


#Checks the guess provided by the player
def checks_the_guess():
    global counter
    global blank
    global alphabet

    guess = input("Please guess a letter: ")
    guess = guess.upper()
    valid = False
    #Makes sure the input is valid
    while not valid:
        if len(guess) == 1 and guess in alphabet:
            valid = True

        #Asks the player for another input if the input was invalid
        else:
            guess = input("Invalid Guess. Please guess a letter: ")
            guess = guess.upper()

    #If the guess is correct
    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i]==guess:
                blank[i] = guess
        print(f'Good Job, {guess} is in the word')

    #If the guess is valid but incorrect
    else:
        #Makes sure the same wrong answer isn't counted twice
        alphabet = alphabet.replace(guess, '')
        print(f'{guess} is not in the word\n')
        counter += 1


#Asks the player if they want to play again
def play_again():
    global alphabet
    global counter
    again = input('Play Again? (Y/N): ')
    again = again.upper()

    while again not in ["Y", "N"]:
        again = input("Invalid answer. Choose: (Y/N) ")
        again = again.upper()
        if again in ["Y", "N"]:
            break

    if again == 'Y':
        #Reassigns the characters for new game
        alphabet = 'QWERTYUIOPLKJHGFDSAZXCVBNM'
        counter = 0
        play_game()
    else:
        return


#--------Executes the game--------
play_game()