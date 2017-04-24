# ex_2.py
# By Aspen
# Work with a nested dictionary

ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

print("\nNested Dictionary Exercises: Ramit")
print("ramit = ", ramit)

print("\n1. Write an expression that gets Ramit's email address.")
print("ramit.get('email'):", ramit.get('email'))
print("ramit['email']:", ramit['email'])

print("\n2. Write an expression that gets Ramit's first interest.")
print("ramit['interests'][0]:", ramit['interests'][0])

print("\n3. Write an expression that gets Jasmine's email address.")
print("ramit['friends'][0]['email']:", ramit['friends'][0]['email'])

print("\n4. Write an expression that gets Jan's second interest.")
print("ramit['friends'][1]['interests'][1]:", \
 ramit['friends'][1]['interests'][1])
