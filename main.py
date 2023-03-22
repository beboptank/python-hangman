import random


def create_blank_word(word):
    blank_word = []

    for letter in word:
        blank_word.append("_")

    return blank_word


word_list = ["monkey", "cat", "building", "interstate", "buddy"]

chosen_word = random.choice(word_list)

user_letter = input("Guess a letter: ").lower()

contains_letter = chosen_word.find(user_letter)

for i in chosen_word:
    if i == user_letter:
        print("Right")
    else:
        print("Wrong")

blank_word = create_blank_word(chosen_word)

print(blank_word)
