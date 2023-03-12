import random

word_list = ["monkey", "cat", "building", "interstate", "buddy"]

chosen_word = word_list[random.randint(0, 4)]

user_letter = input("Guess a letter: ")

contains_letter = chosen_word.find(user_letter)

for i in chosen_word:
    if i == user_letter:
        print("Right")
    else:
        print("Wrong")

