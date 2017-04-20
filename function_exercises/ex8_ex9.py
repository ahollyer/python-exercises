# Asks the user to play again

def play_again():
    while True:
        answer = input("Do you want to play again? Y or N? ").upper()
        if answer == "Y":
            return True
        elif answer == "N":
            return False
        else:
            print("\nThat is not a valid answer. Please type y or n.")

if __name__ == "__main__":
    play_again()
