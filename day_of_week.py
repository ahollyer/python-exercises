# day_of_week.py
# by Aspen
# Accepts a number and returns the corresponding day of the week

def main():

    while True:
        try:
            num = int(input("Enter a number from 0-6: "))
            break
        except ValueError:
            print("Your input must be a number. Try again.")

    def day_of_week(num):
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

        if num < len(days):
            print("You chose {num}. The corresponding weekday is {day}.".format(num=num, day=days[num]))
            return
        else:
            print("The number you chose has no corresponding weekday. Please choose a number from 0-6.")


    day_of_week(num)

main()
