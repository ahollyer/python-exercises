# day_of_week.py
# by Aspen
# Accepts an integer 0-6 and prints the corresponding weekday as a string

def main():

    def day_of_week():
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

        while True:
            try:
                num = int(input("Enter a number from 0-6: "))
                print("You chose {num}. The corresponding weekday is {day}.".format(num=num, day=days[num]))
                break
            except ValueError:
                print("Your input must be a number. Try again.")
            except IndexError:
                print("The number you chose has no corresponding weekday. Please choose a number from 0-6.")


    day_of_week()

main()
