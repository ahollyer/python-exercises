# ex_1.py
# By Aspen
# Modifies a simple dictionary

phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

print("\nDictionary Exercises: Phonebook")
print("phonebook_dict = ", phonebook_dict)

print("\n1. Print Elizabeth's phone number:")
print("Elizabeth's Number bracket:", phonebook_dict['Elizabeth'])
print("Elizabeth's Number .get():", phonebook_dict.get('Elizabeth'))

print("\n2. Add an entry to the dictionary.")
phonebook_dict['Kareem'] = '968-345-2345'
print(phonebook_dict)

print("\n3. Delete Alice's phone entry.")
del phonebook_dict['Alice']
print(phonebook_dict)

print("\n4. Change Bob's phone number.")
phonebook_dict['Bob'] = '968-345-2345'
print(phonebook_dict)

print("\n5. Print all the phonebook entries.")
for key, value in phonebook_dict.items():
    print(key + ": " + value)
