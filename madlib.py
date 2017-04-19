# madlib.py
# by Aspen Hollyer
# Asks for input as strings, generates and prints a madlib string

def main():

    name = input("Give me a name: ")
    subject = input("Give me a school subject: ")
    pet = input("Give me an animal: ")
    power = input("Give me a superpower: ")
    food = input("Give me a food: ")
    num = input("Give me a number: ")

    def madlib(name, subject, pet, power, food, num):
        print("{name}'s {pet} ate some magical {food} that granted him the power of {power}. It also made him a genius! He went on to major in {subject} and win a nobel prize at the age of {num}. The end.".format(name=name, pet=pet, food=food, power=power, subject=subject, num=num))

    madlib(name, subject, pet, power, food, num)

main()
