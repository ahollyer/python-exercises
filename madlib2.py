# madlib.py
# by Aspen Hollyer
# Asks for input as strings, generates and prints a madlib string

# Get words from user
def get_input():
    words = {}
    words['name'] = input("Give me a name: ")
    words['subject'] = input("Give me a school subject: ")
    words['pet'] = input("Give me an animal: ")
    words['power'] = input("Give me a superpower: ")
    words['food'] = input("Give me a food: ")
    words['num'] = input("Give me a number: ")
    return words

# Print madlib with user's words
def madlib(dict_of_words):
    print("%(name)s's %(pet)s ate some magical %(food)s that granted him the power of %(power)s. It also made him a genius! He went on to major in %(subject)s and win a nobel prize at the age of %(num)s. The end." % dict_of_words)


def main():

    words = get_input()
    madlib(words)

main()
