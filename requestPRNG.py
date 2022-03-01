import time
from random import seed
from random import randint, random

# This is a PRNG microservice program.

# It generates a pseudo-random number.

# After the UI writes "request" to the text file, it then calls this program.

# This program opens the text file, verifies the word "request", erases it, and replaces it with
# the pseudo-random integer.

# Note that I can comment out any of the print statements that print to the console.
# This basically lasts for around 5000 seconds, and checks for the word "request" every five seconds.
# If request is there, this microservice generates a new random integer from -100 to 100
# and writes it to the second text file.

print ('Starting PRNG-microservice process.')


for z in range (1000):

    time.sleep(5)

    f = open("request.txt", "r")
    g = f.read()
    #print(g)
    #g = f.read()

    #print(' *** this is what the PRNG microservice program read from the text file ***')
    #print(g)


    value = randint(1, 999)

    #print(value)

    if (g == "request"):
        print('*** the text file said "request" ***')
        with open('getrequest.txt', 'w') as f:
            f.write(str(value))

    #print(value)


