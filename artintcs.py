# importing the required modules
import datetime
import random
print("FIRST PROGRAM NOW EXECUTING")
print(
    "----------------------------------------------------------------------------------------------------------------------")
print()
# FIRST PROGRAM

print('----WELCOME TO WINDOWS 7 LOGIN SIMULATOR----')
print('----CREATED BY ADITYA VERMA----')
print()
secret_word = "billygates"
guesses = ""
county = 0
count = 2
limit = 3
out = False
print('Enter your password [You have 3 tries]')
while guesses != secret_word and not(out):
    if county < limit:
        guesses = input('Enter you password >>>  ')
        if secret_word != guesses:
            print(f'You have {count} tries left')
            print('Wrong password. Try again...')
        county = county+1
        count = count-1

    else:
        out = True
if out:
    print('You are out of tries...')
else:
    print('Password accepted')
    print('Logging you in...')
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print()
print("WELCOME TO WINDOWS 7")
print(
    "----------------------------------------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------------")
print("SECOND PROGRAM NOW EXECUTING")
# SECOND PROGRAM
print("----WELCOME TO THE TESLA PROGRAM----")
print('----CREATED BY ADITYA VERMA----')
print()
age = int(input('Enter your age here ---->>>    '))
if age < 17 or age == 17:
    print('You can\'t drive now buddy!!---TESLA SHUTTING DOWN')
elif age > 17:
    lis = input('Do you have a driving license ? [Yes/No] ------->>>    ')
    if lis == "yes" or lis == "Yes" or lis == "YES":
        print('You can drive a car! Congrats....')
        hash = random.getrandbits(128)
        print("athunecation key is: %032x" % hash)
        print()
        print("KEY ACCEPTED")
        print("Your Tesla is staring now....")
    else:
        print('You can\'t drive now buddy!!, Get yourself a driving license first--TESLA SHUTTING DOWN')
else:
    print("ERROR")

print("----------------------------------------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------------")
print("THIRD PROGRAM NOW EXECUTING")
# THIRD PROGRAM
print("----WELCOME TO THE STORY PROGRAM----")
print('----CREATED BY ADITYA VERMA----')
print()
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
city = ["Mumbai", "New York", "Delhi", "Tokyo", "Berlin"]
# producing a random value from the list [names]

randomname = random.choice(names)

# producing a random value from the list [roles]

randomrole = random.choice(roles)

# producing a random value from the list [city]

randomcity = random.choice(city)

# printing the final story

print(
    f'Once upon a time, there was a {randomrole} whose name was {randomname} who lived in {randomcity} with his friends and family.')
print("-----------------------------------------CREATED BY ADITYA VERMA-----------------------------------------------------------------------")
print("-----------------------------------------CREATED BY ADITYA VERMA-----------------------------------------------------------------------")
print("-----------------------------------------CREATED BY ADITYA VERMA-----------------------------------------------------------------------")
print("-----------------------------------------CREATED BY ADITYA VERMA-----------------------------------------------------------------------")
print("-----------------------------------------CREATED BY ADITYA VERMA-----------------------------------------------------------------------")
