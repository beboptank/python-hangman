import random


def create_blank_word(word):
    # This function creates a list of underscores with a length equal to that of the "word" argument.

    blank_word = []

    for letter in word:
        blank_word.append("_")

    return blank_word


word_list = ["monkey", "cat", "building", "interstate", "buddy", "zebra", "cow", "puppy"]

chosen_word = random.choice(word_list)

user_letter = input("Guess a letter: ").lower()

# contains_letter = chosen_word.find(user_letter)

blank_word = create_blank_word(chosen_word)

for i in range(len(chosen_word)):
    if chosen_word[i] == user_letter:
        blank_word[i] = user_letter

print(blank_word)
