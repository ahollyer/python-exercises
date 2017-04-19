# tip_calc.py
# by Aspen
# Accepts a bill amount, service level, and number of patrons. Prints price per patron including appropriate tip.

print("\n***\nINSTRUCTIONS: This program accepts your bill amount, number of patrons, and level of satisfaction with your service. It splits your check and returns the price per patron including appropriate tip.\n***\n")

def main():
    # ask for bill amount
    bill = float(input("What is the amount of your bill? $"))

    # ask for number of patrons
    num_guests = int(input("How many people are splitting the check? "))

    # ask for satisfaction level
    service = input("\nHow was the service?\ngood\nfair\nbad\nPlease type one of the above options, then press Enter. ").lower()


    # calculate tip amount
    tips = {"good" : 0.20,
            "fair" : 0.15,
            "bad" : 0.10}
    tip_percentage = tips[service]
    tip = bill * tip_percentage

    # calculate cost per guest
    cost_per_guest = (bill + tip) / num_guests

    # print message with tip amount
    print("\nYour bill was ${bill:.2f}, and your service was {service}. You should tip ${tip:.2f}.\n\nEach guest owes ${cost_per_guest:.2f}.".format(bill=bill, service=service, tip=tip, cost_per_guest=cost_per_guest))

main()
