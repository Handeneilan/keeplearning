#import the random module
import random
from hangmanart import stages, logo
from words import word_list

print(logo)

end_of_game = False

#random word generator
chosen_word = random.choice(word_list)
word_lenght = len(chosen_word)

# Create a variable called 'lives' to keep track of the number of lives left. 
# Set 'lives' to equal 6.
lives = 6

# create empty list to hold choosen word.
list = []

# adding blanks in the list
for _ in range(word_lenght):
    list += "_"

while not end_of_game:
    # Ask the user to guess a letter
    guess = input("Please guess a letter: ").lower()

    if guess in list:
        print(f"You've already guessed {guess}")

    #Check if the letter the user guessed (guess) is one of the letters in the chosen_word by creating the position variable.
    for position in range(word_lenght):
        letter = chosen_word[position]
       # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            list[position] = letter

    #If guess is not a letter in the chosen_word,Then reduce 'lives' by 1. If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(list)}")

    #Check if user has got all letters.
    if "_" not in list:
        end_of_game = True
        print("You Win!")
    
    #print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])