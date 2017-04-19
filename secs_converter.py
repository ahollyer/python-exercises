# secs_converter.py
# By Aspen & Sammy
# Asks for a number of seconds and prints the corresponding number of hours, days, and years

def main():

    secs = int(input("How many seconds does it take? "))
    mins = secs / 60
    hours = mins / 60
    days = hours / 24
    years = days / 365

    print("It takes", secs, "seconds. That's a lot of time.\nThat's", hours, "hours.\nThat's", days, "days.\nThat's", years, "years.\nWow!")

main()
