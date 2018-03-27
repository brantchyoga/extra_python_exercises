# Guessing Game
from random import *
# Create a program that asks the user to guess a number between 1 and 100.

# Once the user guesses a number, the program should say, higher, lower, or
# tell the user that he got the number correct. The user should continue to
# make guesses until he guesses correctly. Also, once the user guesses correctly,
# the program should print the number of guesses needed to arrive at the correct answer.

# Below is sample output:


# Guess a number between 1 and 100
# 50 <-- user input
# The number is lower than 50.  Guess again
# 25
# The number is lower than 25.  Guess again
# 13
# The number is higher than 13.  Guess again
# 20
# The number is lower than 20.  Guess again
# 17
# The number is higher than 17.  Guess again
# 18
# The number is higher than 18.  Guess again
# 19
# You got it in 7 tries


# HINT:
# To get input from a user use the input() method:
# num_of_cookies = input("How many cookies should I eat?")
# num = int(num)

# This will assign the typed input value to your variable as a number

random_number = int(random()*100)
counts = 1
def cookies(counts,guess):
    if (int(guess)>random_number):
        guess = input(f'the number is you should eat is less than {guess}. Guess Agian!')
    elif (int(guess)<random_number):
        guess = input(f'the number is you should eat is more than {guess}. Guess Agian!')
    if int(guess)==random_number:
        print(f'Correct you guessed the amount of cookies to eat in {counts} tries. {guess} cookies!')
    else:
        counts += 1
        cookies(counts,guess)
guess = input("How many cookies should I eat?")
cookies(counts,guess)

def cooky():
    guess = input("How many cookies should I eat?")
    guesses = 1
    if int(guess)==random_number:
        print(f'Correct you guessed the amount of cookies to eat in {guesses} tries. {guess} cookies!')
    else:
        while int(guess) != random_number:
            guesses += 1
            if (int(guess)>random_number):
                guess = input(f'the number is you should eat is less than {guess}. Guess Agian!')
            elif (int(guess)<random_number):
                guess = input(f'the number is you should eat is more than {guess}. Guess Agian!')
        print(f'Correct you guessed the amount of cookies to eat in {guesses} tries. {guess} cookies!')
# cooky()
