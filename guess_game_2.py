# guess_game_2.py
# By Aspen
# A program that guesses a number from 1-100 chosen by you.

def guess():
    playing = True
    min = 1
    max = 100
    guess_count = 0

    while playing:

        # Update guess with new min/max values
        current_guess = int((min + max)/2)
        # Accumulate guesses
        guess_count += 1
        # Guess a number
        print("Is it {current_guess}?".format(current_guess=current_guess))
        # Ask user if guess is correct
        answer1 = input("Type Y or N: ").lower()

        if answer1 == 'y':
            # Print win message
            print("I win! Your number is {current_guess}. It only took me {guess_count} guesses.".format(current_guess=current_guess, guess_count=guess_count))
            # Stop playing
            playing = False

        elif answer1 == 'n':
            # Ask user if guess was too high or too low
            print("Was my guess too high or too low?")
            answer2 = input("Type H or L: ").lower()
            # Update range of possible guesses to reflect user input
            if answer2 == 'h':
                max = current_guess - 1
            elif answer2 == 'l':
                min = current_guess + 1


def play():
    input("Ready? Don't tell me your number. Press ENTER to begin. ")
    guess()

def main():
    print("\n***\nINSTRUCTIONS: Hello. I am GuessBot. Choose a number from 1-100. I will try to guess your number.\n***\n")

    play()

main()
