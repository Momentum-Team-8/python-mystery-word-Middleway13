# import module
# to be called in future function
import random

# create user input
guess = input("Press 'enter' to start 'Mystery Word'")

# random word list
words = [
    "rainbow",
    "united",
    "salvation",
    "creation",
    "truth",
    "light",
    "forever",
    "father",
    "spirit",
    "water",
    "wisdom",
    "repentance",
    "understanding",
]

# function will choose random word from list
word = random.choice(words)

# number of turns
turns = 13

# guesses made
guesses = []
correct = []
incorrect = []

while turns > 0:

    # show game progress of
    # correct letters and placement
    progress = []

    # counted failed guesses
    failed = 0

    # take guesses and...
    for letter in word:

        # compare with the letter in word
        if letter in guesses:
            print(letter)

        else:
            print("_")

            # for every incorrect, 1 will be added to failed
            failed += 1
    # props to Roan for lines 58-66
    for letter in word:
        if guesses == letter:
            progress.append(guesses)
            correct.append(guesses)
        elif letter in correct:
            progress.append(letter)
        else:
            incorrect.append(guesses)
    print(guesses)

    # win the game if failure is 0
    if failed == 0:
        print("You win! Yay!")

        # print the correct word
        print("The word is:", word)
        break
    # if incorrect guess
    # then ask for another letter
    guess = input("guess a letter:")

    # every guess letter will be stored in guesses
    guesses += guess

    # compare guess with the letter in word
    if guess not in word:

        turns -= 1

        # if the guess doesn’t match the word
        print("Wrong guess")

        # print the number of turns left
        print("You have", +turns, "more guesses")

        if turns == 0:
            print("You lose!")
            print("The word was:", word)
