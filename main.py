# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# how read text file

from tkinter import *
from tkinter import ttk


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="шестьдесят :)").grid(column=0, row=0)
ttk.Button(frm, text="Click to type number", command=root.destroy).grid(column=1, row=0)
root.mainloop()


russianNumber = int(input('Enter a number: '))

oneNine = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
thirtyNinety = ["тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
twoHundredfiveHundred = ["двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]

print(oneNine[1])

bitStream = ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
keyGen = ["1", "0", "1", "0", "1", "0", "1", "0", "1", "0"]
bitOutput = ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
decimalOutput = 0

for x in range(9):
    if (bitStream[x] == keyGen[x]):
        bitOutput[x]="0"
        decimalOutput=decimalOutput+(2**(x))
        print (decimalOutput)

print('bs', bitStream[0], 'k', keyGen[0], 'bo', bitOutput[0])

russianNumber1=decimalOutput



if ((russianNumber//512)>0):
    bitStream[0]=1


#if ((russianNumber%2) == 0):
    #bitStream[0] = "0"

if ((russianNumber > 8)):       # need an elegant way to convert to binary; also need to do an XOR
    bitStream[3] = "1"

#f = open("один_девять.txt", "r")
#print(f.read())

#with open("один_девять.txt") as f:
#    contents = f.read()
#    print(contents)

russianHundreds=russianNumber//100 #integer division for hundreds column
russianTens=(russianNumber%100)//10      #internet division for tens column

print('tens= ', russianTens)

russianNumber=russianNumber%10

print('один два три четыре пять')

print(twoHundredfiveHundred[russianHundreds-2], thirtyNinety[russianTens-3], oneNine[russianNumber-1])

print('    NOW WE ADD A RANDOM KEY K FROM A MICROSERVICE TO RANDOMIZE THE NEXT FLASHCARD.')
KEYKEY = input('*** HIT ANY KEY TO PULL A RANDOM KEY FROM A MICROSERVICE')

print('The binary equivalent of your number is:')
print(bitStream[3], bitStream[2], bitStream[1], bitStream[0])
print('The binary value of the key k is:')
print(bitStream)
print('The XOR of these two numbers is:')
print(keyGen)
print('The random number generated (in Russian) is:')
print(bitOutput)

russianHundreds=russianNumber1//100 #integer division for hundreds column
russianTens=(russianNumber1%100)//10      #internet division for tens column
goodValue=russianNumber1
russianNumber1=russianNumber1%10
print('shhhh...the encrypted number is (just for testing purposes', russianHundreds, russianTens, russianNumber1)



print('The encrypted number is: ', twoHundredfiveHundred[russianHundreds-2], thirtyNinety[russianTens-3], oneNine[russianNumber1-1])

answer = int(input('What is this new encrypted number? '))



if (answer == goodValue):
    print('YOU ARE CORRECT!')
else:
    print ('YOU ARE WRONG.')




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
