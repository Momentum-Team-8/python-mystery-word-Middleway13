import random

# random word list

guess = input("Guess a letter to start 'Mystery Word'")


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


guesses = ""

# number of turns
turns = 13
