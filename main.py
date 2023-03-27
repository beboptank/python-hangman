import random
from string import Template


def create_blank_word(word):
    # This function creates a list of underscores with a length equal to that of the "word" argument.

    solution = []

    for _ in word:
        solution.append("_")

    return solution


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
        print(answer_template)
        print("***PLEASE TRY AGAIN***")
        return
    else:
        print("Error. Please restart the game.")
        return


word_list = ["monkey", "cat", "building", "interstate", "buddy", "zebra", "cow", "puppy"]

chosen_word = random.choice(word_list)

# contains_letter = chosen_word.find(user_letter)

blank_word = create_blank_word(chosen_word)

display_graphics()

guess_counter = 0

while "_" in blank_word:
    hangman(guess_counter)
    user_letter = input("Guess a letter: ").lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == user_letter:
            blank_word[i] = user_letter
            guess_counter += 1
    print(blank_word)

answer = "".join(blank_word)
answer_template = Template("The answer was ${answer}.")

print("***CONGRATULATIONS***")
print("***YOU WIN***")
print(answer_template)
