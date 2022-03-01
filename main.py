# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# how read text file

from tkinter import *
from tkinter import ttk
from tkinter import Tk
from tkinter.font import BOLD, Font
from tkinter.ttk import Label\


# generate random integer values
from random import seed
from random import randint
# seed random number generator
#seed(1) otherwise, with seed(1), the same list of random numbers will be generated each time...
# generate some integers
for x in range(9):
	value = randint(1, 999)
	print(value)

root = Tk()
frm = ttk.Frame(root, padding=250)
frm.grid()
#label = Label(root, text="PASS", bg="green", fg="black", font=(None, 15), height=50, width=50)
ttk.Label(frm, text="Привет! (Hello!)", font=(None, 18), background="green", foreground="white").grid(column=0, row=0)

g = open("request.txt", "w")
g.write('request')
g.close()

#ttk.Label(frm, text="Привет! (Hello!)", font=(None, 18), background="blue", foreground="red").grid(column=0, row=1)
ttk.Button(frm, text="   Click to type a number in the console, and then we will translate it into Russian words.", command=root.destroy).grid(column=1, row=0)
root.mainloop()

fauxKey = int(input('Do you want to manually enter a three digit number to use as a key?  Enter a number from 1-999:'))

# OVERRIDE

fauxKey=value



g = open("keyFile.txt", "w")
g.write(str(fauxKey))
g.close()


# modifying this 2/28/2022 to read getrequest.txt instead of keyFile.txt, and add 200 to it
with open('getrequest.txt') as f:
    lines = f.read()

print(lines, fauxKey)

keyPlus = int(lines)

#keyPlus = keyPlus + 200

print(keyPlus)

russianNumber = int(input('Enter a number: '))

oneNine = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
thirtyNinety = ["двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
twoHundredfiveHundred = ["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]

#print(oneNine[1])

bitStream = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
gStream = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
kStream = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
keyGen = ["1", "0", "1", "0", "1", "0", "1", "0", "1", "0"]
bitOutput = ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
decimalOutput = 0
dummyNumber = russianNumber
gNumber = dummyNumber
kNumber = keyPlus

for y in range(10):
    if ((gNumber//(2**(9-y)))>0):
        gStream[y]="1"
        gNumber=gNumber%(2**(9-y))

for z in range(10):
    if ((kNumber//(2**(9-z)))>0):
        kStream[z]="1"
        kNumber=kNumber%(2**(9-z))


print('GSTREAM ', gStream, gNumber)
print('KSTREAM', kStream)

if ((russianNumber//512)>0):
    bitStream[0]="1"
    dummyNumber = dummyNumber%512



if ((dummyNumber//256)>0):
    bitStream[1]="1"
    dummyNumber = dummyNumber%256


if ((dummyNumber//128)>0):
    bitStream[2]="1"
    dummyNumber = dummyNumber%128


if ((dummyNumber//64)>0):
    bitStream[3]="1"
    dummyNumber = dummyNumber%64

if ((dummyNumber//32)>0):
    bitStream[4]="1"
    dummyNumber = dummyNumber%32

if ((dummyNumber//16)>0):
    bitStream[5]="1"
    dummyNumber = dummyNumber%16

if ((dummyNumber//8)>0):
    bitStream[6]="1"
    dummyNumber = dummyNumber%8

if ((dummyNumber//4)>0):
    bitStream[7]="1"
    dummyNumber = dummyNumber%4

if ((dummyNumber//2)>0):
    bitStream[8]="1"
    dummyNumber = dummyNumber%2

if ((dummyNumber//1)>0):
    bitStream[9]="1"
    #dummyNumber = dummyNumber//64

for x in range(10):
    if (bitStream[x] == kStream[x]):
        bitOutput[x]="0"
    else:
        decimalOutput=decimalOutput+(2**(9-x))


russianNumber1=decimalOutput

#if ((russianNumber%2) == 0):
    #bitStream[0] = "0"



#f = open("один_девять.txt", "r")
#print(f.read())

#with open("один_девять.txt") as f:
#    contents = f.read()
#    print(contents)

russianHundreds=russianNumber//100 #integer division for hundreds column
russianTens=(russianNumber%100)//10      #internet division for tens column

#print('tens= ', russianTens)

russianNumber=russianNumber%10

#print('один два три четыре пять')

print(twoHundredfiveHundred[russianHundreds-1], thirtyNinety[russianTens-2], oneNine[russianNumber-1])

print('    NOW WE ADD A RANDOM KEY K FROM A MICROSERVICE TO RANDOMIZE THE NEXT FLASHCARD.')
#KEYKEY = input('*** H" "


XOR = " "
KEY = " "
OUT = " "




for x in range(10):
    XOR = XOR+bitOutput[x]
    KEY = KEY+kStream[x]
    OUT = OUT+bitStream[x]
    print (XOR)

print('The binary equivalent of your number is:')
print(OUT)

print('The binary value of the key k is:')
#print(keyGen)
print(KEY)
print('The XOR of these two numbers is:')
#print(bitOutput)
print(XOR)

M = OUT + (" MSG")
K = KEY + (" KEY")
X = XOR + (" XOR")

root = Tk()
frm = ttk.Frame(root, padding=250)
frm.grid()
#label = Label(root, text="PASS", bg="green", fg="black", font=(None, 15), height=50, width=50)
ttk.Label(frm, text="Here is the binary representation of the message, random key, and the XOR of the two values:", font=(None, 15)).grid(column=0, row=0)
ttk.Label(frm, text=M, font=(None, 28), background="green", foreground="red").grid(column=0, row=2)
ttk.Label(frm, text=K, font=(None, 28), background="blue", foreground="red").grid(column=0, row=3)
ttk.Label(frm, text=X, font=(None, 28), background="yellow", foreground="red").grid(column=0, row=4)
ttk.Button(frm, text="   Click to continue...", command=root.destroy).grid(column=1, row=1)
root.mainloop()


#print(bitOutput)

russianHundreds=russianNumber1//100 #integer division for hundreds column
russianTens=(russianNumber1%100)//10      #internet division for tens column
goodValue=russianNumber1
russianNumber1=russianNumber1%10
print('***  shhhh...the encrypted number is (just for testing purposes', russianHundreds, russianTens, russianNumber1, '  ***')



summation = twoHundredfiveHundred[russianHundreds-1] + " " + thirtyNinety[russianTens-2] + " " + oneNine[russianNumber1-1]
if (russianHundreds==0):
    summation = thirtyNinety[russianTens-2] + " " + oneNine[russianNumber1-1]

if (russianNumber1==0):
    summation = twoHundredfiveHundred[russianHundreds-1] + " " + thirtyNinety[russianTens-2]

print('The random number generated (in Russian) is:', summation)

root = Tk()
frm = ttk.Frame(root, padding=300)
frm.grid()
ttk.Label(frm, text=summation, font=(None, 22), foreground="red").grid(column=0, row=0)

ttk.Label(frm, text="Here is a randomly generated Russian number.  ", font=(None, 15)).grid(column=0, row=3)
ttk.Label(frm, text="This was generated using a cryptographic algorithm called ONE TIME PAD, ", font=(None, 15)).grid(column=0, row=4)
ttk.Label(frm, text="which takes your original input message and transforms it by taking the XOR", font=(None, 15)).grid(column=0, row=5)
ttk.Label(frm, text="logical operation between your original number and a random key generated", font=(None, 15)).grid(column=0, row=6)
ttk.Label(frm, text="by a microservice provided by my teammate.", font=(None, 15)).grid(column=0, row=7)

# fred = Button(self, fg="red", bg="blue")

ttk.Button(frm, text="TRANSLATE THIS!", command=root.destroy).grid(column=1, row=0)
root.mainloop()

#print('The encrypted number is: ', twoHundredfiveHundred[russianHundreds-1], thirtyNinety[russianTens-2], oneNine[russianNumber1-1])
print('The encrypted number is: ', summation)

answer = int(input('What is this new encrypted number? '))



if (answer == goodValue):
    print('YOU ARE CORRECT!')
else:
    print ('YOU ARE WRONG.')




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
