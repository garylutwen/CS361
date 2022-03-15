# Gary Lutwen

from tkinter import *
from tkinter import ttk
from tkinter import Tk
from tkinter.font import BOLD, Font
from tkinter.ttk import Label\


# generate random integer values (replaced by microservice)
#from random import seed
#from random import randint


root = Tk()
frm = ttk.Frame(root, padding=250)
frm.grid()

# WRITES TO FILE AS PIPE FOR MICROSERIVCE
g = open("instruction.txt", "w")
g.write('run')
g.close()

ttk.Label(frm, text="Привет! (Hello!)", font=(None, 18), background="green", foreground="white").grid(column=0, row=0)
ttk.Button(frm, text="   Click to type a number in the console, and then we will translate it into Russian words.", command=root.destroy).grid(column=1, row=0)
root.mainloop()

# WRITES TO FILE AS PIPE FOR MICROSERIVCE
g = open("instruction.txt", "w")
g.write('run')
g.close()

# READS DATA FROM FILE AS PIPE FROM MICROSERVICE
with open('test.txt') as f:
    lines = f.read()

# CONVERTS TEXT TO INTEGER FOR USE IN THIS APPLICATION
keyPlus = int(lines)

print('My teammates random key is: ', keyPlus)


# ASKS USER TO ENTER AN INTEGER TO BE TRANSCRIBED INTO RUSSIAN WORDS
russianNumber = int(input('Enter a number: '))

oneNine = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
thirtyNinety = ["двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
twoHundredfiveHundred = ["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]


# INITIALIZATION OF ALL BITSTREAMS
bitStream = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
gStream = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
kStream = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
bitOutput = ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]

decimalOutput = 0
dummyNumber = russianNumber
gNumber = dummyNumber
kNumber = keyPlus


# CREATION OF BITSTREAMS FOR USER INPUT AND RANDOM KEY
for y in range(10):
    if ((gNumber//(2**(9-y)))>0):
        gStream[y]="1"
        bitStream[y]="1"
        gNumber=gNumber%(2**(9-y))

for z in range(10):
    if ((kNumber//(2**(9-z)))>0):
        kStream[z]="1"
        kNumber=kNumber%(2**(9-z))

# DETERMINES XOR BITSTREAM OF USER INPUT AND RANDOM KEY
for x in range(10):
    if (bitStream[x] == kStream[x]):
        bitOutput[x]="0"
    else:
        decimalOutput=decimalOutput+(2**(9-x))

# DETERMINE HUNDREDS, TENS, AND ONES INTEGER VALUES TO TRANSLATE TO RUSSIAN
russianNumber1=decimalOutput
russianHundreds=russianNumber//100          #integer division for hundreds column
russianTens=(russianNumber%100)//10         #integer division for tens column
russianNumber=russianNumber%10


print(twoHundredfiveHundred[russianHundreds-1], thirtyNinety[russianTens-2], oneNine[russianNumber-1])


root = Tk()
frm = ttk.Frame(root, padding=250)
frm.grid()

ttk.Label(frm, text="Your number, translated into Russian, is:", font=(None, 15)).grid(column=0, row=0)
ttk.Label(frm, text=dummyNumber, font=(None, 20), background="pink").grid(column=0, row=1)
ttk.Label(frm, text=twoHundredfiveHundred[russianHundreds-1], font=(None, 28), background="green", foreground="pink").grid(column=0, row=2)
ttk.Label(frm, text=thirtyNinety[russianTens-2], font=(None, 28), background="blue", foreground="pink").grid(column=0, row=3)
ttk.Label(frm, text=oneNine[russianNumber-1], font=(None, 28), background="yellow", foreground="pink").grid(column=0, row=4)
ttk.Button(frm, text="   Click to continue...", command=root.destroy).grid(column=1, row=1)
root.mainloop()




print('    NOW WE ADD A RANDOM KEY K FROM A MICROSERVICE TO RANDOMIZE THE NEXT FLASHCARD.')

XOR = " "
KEY = " "
OUT = " "
TEST = " "



# CREATING VISUAL BITSTREAMS FROM ALL ARRAYS
for x in range(10):
    XOR = XOR+bitOutput[x]
    KEY = KEY+kStream[x]
    OUT = OUT+bitStream[x]

print('The binary equivalent of your number is:')
print(OUT)

print('The binary value of the key k is:')
print(KEY)

print('The XOR of these two numbers is:')
print(XOR)

M = OUT + (" MSG")
K = KEY + (" KEY")
X = XOR + (" XOR")

root = Tk()
frm = ttk.Frame(root, padding=250)
frm.grid()

ttk.Label(frm, text="Here is the binary representation of the message, random key, and the XOR of the two values:", font=(None, 15)).grid(column=0, row=0)
ttk.Label(frm, text=M, font=(None, 28), background="green", foreground="red").grid(column=0, row=2)
ttk.Label(frm, text=K, font=(None, 28), background="blue", foreground="red").grid(column=0, row=3)
ttk.Label(frm, text=X, font=(None, 28), background="yellow", foreground="red").grid(column=0, row=4)
ttk.Button(frm, text="   Click to continue...", command=root.destroy).grid(column=1, row=1)
root.mainloop()



# TRANSCRIBES ENCRYPTED NUMBER INTO RUSSIAN TO GENERATE A RANDOM FLASH CARD
russianHundreds=russianNumber1//100         #integer division for hundreds column
russianTens=(russianNumber1%100)//10        #integer division for tens column
goodValue=russianNumber1
russianNumber1=russianNumber1%10

print('***  shhhh...the encrypted number is (just for testing purposes) is: ', russianHundreds, russianTens, russianNumber1, '  ***')

summation = twoHundredfiveHundred[russianHundreds-1] + " " + thirtyNinety[russianTens-2] + " " + oneNine[russianNumber1-1]
if (russianHundreds==0):
    summation = thirtyNinety[russianTens-2] + " " + oneNine[russianNumber1-1]

if (russianNumber1==0):
    summation = twoHundredfiveHundred[russianHundreds-1] + " " + thirtyNinety[russianTens-2]


root = Tk()
frm = ttk.Frame(root, padding=300)
frm.grid()
ttk.Label(frm, text=summation, font=(None, 22), foreground="red").grid(column=0, row=0)

ttk.Label(frm, text="Here is a randomly generated Russian number.  ", font=(None, 17)).grid(column=0, row=3)
ttk.Label(frm, text="This was generated using a cryptographic algorithm called ONE TIME PAD, ", font=(None, 15)).grid(column=0, row=4)
ttk.Label(frm, text="which takes your original input message and transforms it by taking the XOR", font=(None, 15)).grid(column=0, row=5)
ttk.Label(frm, text="logical operation between your original number and a random key generated", font=(None, 15)).grid(column=0, row=6)
ttk.Label(frm, text="by a microservice provided by my teammate.", font=(None, 15)).grid(column=0, row=7)
ttk.Label(frm, text="Similar math (modulus,integer division) was used for both translation to Russian & bitstreams.", font=(None, 12)).grid(column=0, row=8)


ttk.Button(frm, text="TRANSLATE THIS!", command=root.destroy).grid(column=1, row=0)
root.mainloop()

print('The encrypted number (in Russian) is: ', summation)

answer = int(input('What is this new encrypted number? '))


# VERIFIES USER INPUT VERSUS CALCULATED INPUT
if (answer == goodValue):
    print('YOU ARE CORRECT!')
else:
    print ('YOU ARE WRONG.')

root = Tk()
frm = ttk.Frame(root, padding=250)
frm.grid()

ttk.Label(frm, text="GREAT JOB!", font=(None, 35)).grid(column=0, row=0)
ttk.Label(frm, text=answer, font=(None, 20), background="pink").grid(column=0, row=1)
ttk.Label(frm, text="Молодец !!", font=(None, 40), background="blue", foreground="pink").grid(column=0, row=2)

ttk.Button(frm, text="   Click to continue...", command=root.destroy).grid(column=1, row=1)
root.mainloop()



