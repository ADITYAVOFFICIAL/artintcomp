# importing random module
import random
# greeting the reader
print("Hello reader")
# Obtaining the the name of the reader
readername = input("What is your name? ")
# printing the name of the reader
print("Hello "+readername)
# creating some lists for our story
names = ["Aditya", "Harsh", "Kamal", "Dipayan", "Dhruv"]  # contains names
roles = ["Chemical Engineer", "Mechanical Engineer",
         "Electrical Engineer", "Software Engineer", "Aeronautical engineer"]  # contains roles or jobs
# producing a random value from the list names
randomname = random.choice(names)
# producing a random value from the list roles
randomrole = random.choice(roles)
# printing the final story
print(
    f'Once upon a time, there was a {randomrole} whose name was {randomname}')
