# work_or_sleep_in.py
# by Aspen
# Accepts a number, converts it to the corresponding weekday, and prints an instruction to sleep in or get up.

def main():

    def work_or_sleep():
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

        while True:
            try:
                num = int(input("Enter a number from 0-6: "))
                if 0 < num < 6:
                    print("It's ", days[num], ". Go to work!", sep="")
                else:
                    print("It's ", days[num], ". Go back to bed!", sep="")
                break
            except ValueError:
                print("Your input must be a number. Try again.")
            except IndexError:
                print("The number you chose has no corresponding weekday. Please choose a number from 0-6.")


    work_or_sleep()

main()
