import random
print("Hello reader")
readername = input("What is your name? ")
print("Hello "+readername)
names = ["Aditya", "Harsh", "Kamal", "Dipayan", "Dhruv"]
roles = ["Chemical Engineer", "Mechanical Engineer",
         "Electrical Engineer", "Software Engineer", "Aeronautical engineer"]
places = ["Mumbai, India", "Delhi, India",
          "Kolkata, India", "Patna, India", "Chennai, India"]
randomname = random.choice(names)
randomplaces = random.choice(places)
randomrole = random.choice(roles)
print(
    f'Once upon a time there was a {randomrole} whose name was {randomname} who lived in {randomplaces}')
