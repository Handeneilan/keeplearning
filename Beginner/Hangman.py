#put a list together
word_list = ["ardvark", "baboon", "camel"]

#import the random module
import random

#random word generator
chosen_word = random.choice(word_list)
#print(chosen_word)

# create empty list to hold choosen word.
list = []
word_lenght = len(chosen_word)

for _ in range(word_lenght):
    list += "_"
print(list)

end_of_game = False
while not end_of_game:
    # Ask the user to guess a letter
    guess = input("Please guess a letter: ").lower()
    #Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    for position in range(word_lenght):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            list[position] = letter
    print(list)

    if "_" not in list:
        end_of_game = True
    print("You Win!")