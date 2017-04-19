# guess_the_number.py
# By Aspen
# Accepts a number and returns whether it is higher than, lower than, or equal to a random number

import random

# assign a secret number
def get_secret_num():
    secret_num = random.randint(1, 100)
    return secret_num

# prompt the user to guess the secret number
def get_guess():
    while True:
        try:
            guess_num = int(input("What's the number? "))
            if 0 < guess_num < 101:
                return guess_num
            else:
                print("Your number must be between 1 and 100. Try again.")
        except ValueError:
            print("Your guess must be an integer (ex: 5). Try again.")

# compare user's guess to secret number
def compare(s, g):
    tries = 4
    win = False
    while not win and tries > 0:
        if g == s:
            print("You win!!")
            win = True
        elif g > s:
            print("Nope, too high. Guesses left:", tries)
            tries -= 1
            g = get_guess()
        elif g < s:
            print("Nope, too low. Guesses left:", tries)
            tries -=1
            g = get_guess()
    print("You ran out of guesses! You lose.")

# ask user to play again
def play_again():
    play = input("Do you want to play again? Yes or no: ").lower()
    if play == 'yes':
        main()
    elif play == 'no':
        print("Okay, bye!")
    else:
        print("That answer doesn't make sense.")
        play_again()

def main():
    print("I'm thinking of a number between 1 and 100. You get 5 tries to guess the number!\n")

    snum = get_secret_num()
    gnum = get_guess()
    compare(snum, gnum)
    play_again()

main()
