# secs_converter.py
# By Aspen & Sammy
# This program accepts a number of seconds and returns a number of minutes, hours, days, and years

def main():
    secs = int(input("How many seconds does it take? "))
    mins = secs / 60
    hours = mins / 60
    days = hours / 24
    years = days / 365

    print("It takes", secs, "seconds. That's a lot of time.\nThat's", hours, "hours.\nThat's", days, "days.\nThat's", years, "years.\nWow!")

main()
