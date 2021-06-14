import random

# random word list

guess = input("Press 'enter' to start 'Mystery Word'")


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

# Function will choose random word from list
word = random.choice(words)


guesses = []

# number of turns
turns = 13

correct = []
incorrect = []
while turns > 0:

    progress = []

    # counts failed guesses
    failed = 0

    # letters from input taking one at a time
    for letter in word:

        # comparing that character with
        # the character in guesses
        if letter in guesses:
            print(letter)

        else:
            print("_")

            # for every failure 1 will be
            # incremented in failure
            failed += 1

    for letter in word:
        if guesses == letter:
            progress.append(guesses)
            correct.append(guesses)
        elif letter in correct:
            progress.append(letter)
        else:
            incorrect.append(guesses)

    if failed == 0:
        # win the game if failure is 0
        # and print 'You Win'
        print("You Win")

        # print the correct word
        print("The word is:", word)
        break
    print(guesses)
    # if incorrect guess then
    # it will ask for another letter
    guess = input("guess a letter:")

    # every guess letter will be stored in guesses
    guesses += guess

    # compare guess with the letter in word
    if guess not in word:

        turns -= 1

        # if the guess doesn’t match the word
        # then print “Wrong"
        print("Wrong")

        # print the number of turns left
        print("You have", +turns, "more guesses")

        if turns == 0:
            print("You lose")
            print("The word was:", word)