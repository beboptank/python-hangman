import random


def create_blank_word(word):
    # This function creates a list of underscores with a length equal to that of the "word" argument.

    blank_word = []

    for letter in word:
        blank_word.append("_")

    return blank_word

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


def hangman(num_of_guesses):
    if num_of_guesses == 0:
        print(""" _____________
             |/      |
             |      
             |      
             |       
             |      
             |
         ____|____""")
    elif num_of_guesses == 1:
        print(""" _____________
             |/      |
             |      (_)
             |      
             |       
             |      
             |
         ____|____""")
    elif num_of_guesses == 2:
        print(""" _____________
             |/      |
             |      (_)
             |       |
             |       |
             |      
             |
         ____|____""")
    elif num_of_guesses == 3:
        print(""" _____________
             |/      |
             |      (_)
             |      \|
             |       |
             |      
             |
         ____|____""")
    elif num_of_guesses == 4:
        print(""" _____________
             |/      |
             |      (_)
             |      \|/
             |       |
             |      
             |
         ____|____""")
    elif num_of_guesses == 5:
        print(""" _____________
             |/      |
             |      (_)
             |      \|/
             |       |
             |      | 
             |
         ____|____""")
    elif num_of_guesses == 6:
        print(""" _____________
             |/      |
             |      (_)
             |      \|/
             |       |
             |      | |
             |
         ____|____""")
    else:
        print("Error. Please restart the game.")


word_list = ["monkey", "cat", "building", "interstate", "buddy", "zebra", "cow", "puppy"]

chosen_word = random.choice(word_list)

# contains_letter = chosen_word.find(user_letter)

blank_word = create_blank_word(chosen_word)

display_graphics()

while "_" in blank_word:
    hangman(0)
    user_letter = input("Guess a letter: ").lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == user_letter:
            blank_word[i] = user_letter
    print(blank_word)


print(blank_word)
