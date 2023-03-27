import random

# Features to be added:
# - add player lives (3 lives per session)
# - prevent user from guessing a previously-guessed letter
# - display to users a running tally of letters guessed

def create_blank_word(word):
    # This function creates a list of underscores with a length equal to that of the "word" argument.

    solution = []

    for _ in word:
        solution.append("_")

    return solution


word_list = ["monkey", "cat", "building", "interstate", "buddy", "zebra", "cow", "puppy"]

chosen_word = random.choice(word_list)

blank_word = create_blank_word(chosen_word)


def display_graphics():
    print("***WELCOME***")
    print("***TO***")
    print(""" _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/     """)
    print("All ASCII art from https://ascii.co.uk/art/hangman")

guess_counter = 0


def hangman(num_of_guesses):
    if num_of_guesses == 0:
        print("""     __________________
             |/      |
             |      
             |      
             |       
             |      
             |
         ____|____""")
    elif num_of_guesses == 1:
        print("""    __________________
             |/      |
             |      (_)
             |      
             |       
             |      
             |
         ____|____""")
    elif num_of_guesses == 2:
        print("""    __________________
             |/      |
             |      (_)
             |       |
             |       |
             |      
             |
         ____|____""")
    elif num_of_guesses == 3:
        print("""    __________________
             |/      |
             |      (_)
             |      \|
             |       |
             |      
             |
         ____|____""")
    elif num_of_guesses == 4:
        print("""    __________________
             |/      |
             |      (_)
             |      \|/
             |       |
             |      
             |
         ____|____""")
    elif num_of_guesses == 5:
        print("""    __________________
             |/      |
             |      (_)
             |      \|/
             |       |
             |      | 
             |
         ____|____""")
    elif num_of_guesses == 6:
        print("""    __________________
             |/      |
             |      (_)
             |      \|/
             |       |
             |      | |
             |
         ____|____""")
        print("***GAME OVER***")
        print("The answer was " + chosen_word + ".")
        print("***PLEASE TRY AGAIN***")
        return
    else:
        print("Error. Please restart the game.")
        return


# contains_letter = chosen_word.find(user_letter)

display_graphics()

while "_" in blank_word:
    hangman(guess_counter)
    user_letter = input("Guess a letter: ").lower()

    if user_letter in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == user_letter:
                blank_word[i] = user_letter

    if user_letter not in chosen_word:
        guess_counter += 1

    print(blank_word)

print("***CONGRATULATIONS***")
print("***YOU WIN***")
print("The answer was " + chosen_word + ".")
