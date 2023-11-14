'''
1. Is a menu that the user can select 5 programs

2. Program 1: program generates a random integer number between 1 and 1,000.  Then it uses the famous binary search algorithm to automatically guess the generated random number.   For each try, count the number of guesses to guess the random number correctly. It will perform this 10000 times once from 1 and 1000 second from 1 and 1000000 it will compute total amount of guesses for both scenarios and the average amount of guesses

3. Program 2: a timeEfficiency() that will test a listPrimeNumbers(theMaxNum) function, which takes an integer (theMaxNum) and list all prime numbers between 0 and theMaxNum sent to the function it Prints out 1) start time, 2) end time, and then 3) time taken to execute the specified function

4. Program 3: A number guessing game that will randomly generate 3 unique numbers from 0 to 9. The computer will then use 2 different algorithms to guess the 3 numbers. Deterministic brute-force algorithm. In each try, it permutates 3 numbers in a deterministic way so that it guesses each set of 3 numbers only once while guessing the 3 random numbers. Pure random algorithm It will not use any prior information to guess the numbers.  For each guess, it makes a fresh new guess for three new numbers randomly from the scratch. It will perform the algotithm 10000 times each and calculate the most guesses it made in one try and the most and least amount of tries as well as the average number of guesses that solved the problem

5. Program 4: program that takes a text file and an integer 'n'  and displays the top ‘n’ number of words in descending order of its occurrences (case insensitive) in the file. 

6. Program 5: Reimplementing timeEfficiency() function using decorators and test it with listPrimeNumber program. 
'''

import random
import time
import itertools
import operator
import os
import os.path

menuOptions = {                  # Menu using dictionary
    1: 'Program 1',
    2: 'Program 2',
    3: 'Program 3',
    4: 'Program 4',
    5: 'Extra Credit',
    6: 'Exit',
}

def printMenu():                 # Function to print menu
    for key in menuOptions.keys(): # loop through keys and print out values
        print (key, '--', menuOptions[key] )

def binarySearch(start, end):          # Makes array from given interval and searches
    tries = 0                          # For random number in array
    randNumber = random.randint(start,end)    
    lower = start
    upper = end
    numList = []
    numList = range(start,end + 1)

    while lower <= upper:              # While the upper bound is bigger than 
        tries += 1
                                       # lower bounds of the search 
        pivot = (lower + upper) // 2   # pick value in middle of bounds 
        pivotVal = numList[pivot]      

        if pivotVal == randNumber:     # If pivot value is the random number return amount of tries made
            return tries
        elif pivotVal > randNumber:    # If pivot value was bigger than random number lower the upper bound
            upper = pivot - 1          # to one less than pivot and search again
        elif pivotVal < randNumber:    # if pivot value is smaller than random number increase lower bounds
            lower = pivot + 1          # to one higher than pivot and search again
    return 0                           # Return 0 if invalid range

def program1():                        # driver for program 1
    count = 0                         # Call the function 10000 times and count total amount of tries of all tries
    totalTries = 0
    while count < 10000:
        totalTries += binarySearch(1, 1000)
        count += 1
    avg = totalTries/10000
    print("\nThe random numbers between 1 .. 1K: Total guesses: " + str(totalTries)+ " Avg: " + str(avg))
    count = 0     
    totalTries = 0       
    while count < 10000:
        totalTries += binarySearch(1, 1000000)
        count += 1
    avg = totalTries/10000
    print("The random numbers between 1 .. 1M: Total guesses: " + str(totalTries) + " Avg: " + str(avg))
    print('\nHandled \'Program 1\'')

def listPrimeNumbers(theMaxNum):        # Makes a new list and fills it with prim numbers to given range
    primeList = []
    for num in range(0, theMaxNum + 1): # Iterate through numbers from 0 to target
        if num > 1:                     # If number reaches number bigger than one
            for i in range(2, num):     # Iterate through all numbers less than the number
                if (num % i) == 0:      # Check if the number is divisible by the number
                    break
            else:                       # If it's not divisible append to list
                primeList.append(num)
    return print("List of prime numbers of " + str(theMaxNum) + "\nresult: " + str(primeList))

def timeEfficiency(funcName, *args):    # Funtion to print time
    time1 = time.process_time()         # Calculate initial proccessing time
    funcName(*args)                     # Execute function
    time2 = time.process_time()         # Get end time
    print("start: " + str(time1) + " end: " + str(time2) + " time efficiency: " + str((time2-time1))) 

def program2():                         # driver for program 2
    mNum = ''                           # Input range for list 
    try:
        mNum = int(input('\nEnter a number for the list of prime numbers: '))
    except:
        print('Wrong input. Please enter a number ...')
    timeEfficiency(listPrimeNumbers, mNum) # call function
    print('\nHandled \'Program 2\'')

def bruteForce(Array):
    tries = 0
    for guess in itertools.permutations(range(0,10), 3): # Using itertools library loops through all
        tries+=1                                         # Combinations beginning from (0,1,2) until (9,8,7)
        if guess == tuple(Array):                        # Compare combination with random numbers via tuples
            break
    return tries                                         # Return number of tires if found

def randGuess(numList):                 # Function that creates a new randomly generated 3 digit array
    guess = []
    tries = 0
    while guess != numList:             # Iterate until the randomly guessed array is the list that is the answer
        tries += 1                              # Increment amount of tries
        guess = random.sample(range(0, 10), 3)  # Generate a 3 digit list from specified range
    return tries                                # Return amount of tries guessed

def program3():                         # Driver for program 3
    highlow = []                        # Create array to story guesses of each tries
    count = 0                           # Count to run both algorithms 10000 times
    print("-----Bruteforce algorithm-----")
    while count < 10000:
        numList = []                    # Create array to store the random numbers to guess
        numList = random.sample(range(0, 10), 3)  # Call function to get guesses
        highlow.append(bruteForce(numList))  # Append guesses to array
        count += 1                      # Increment until 10000
    avg = sum(highlow)/len(highlow)     # Calculate average using the array
    print("Number of Tries: 10000" + "\nThe highest number of guesses in a try: " + str(max(highlow)) + "\nThe lowest number of tries: " + str(min(highlow)) + "\nThe average number of tries: " + str(avg))

    highlow = []                        # Repeat process using random algorithm
    count = 0
    print("\n-----Random Number algorithm-----\nWARNING MAY TAKE A WHILE")
    while count < 10000:
        numList = []
        numList = random.sample(range(0, 10), 3)
        highlow.append(randGuess(numList))
        count += 1
    avg = sum(highlow)/len(highlow)
    print("Number of Tries: 10000" + "\nThe highest number of guesses in a try: " + str(max(highlow)) + "\nThe lowest number of tries: " + str(min(highlow)) + "\nThe average number of tries: " + str(avg))
    print('\nHandled \'Program 3\'')

def fileWordOcc(topNum):
    print("Files in directory: " + str(os.listdir())) # List files in directory using os to interact with operating system
    filename = input("Enter file a file name: ")
    check = os.path.exists(filename)
    if not check:
        return None
    text = open(filename, "r")
    D = dict()                  # Create an empty dictionary
    for line in text:           # Loop through each line of the file
        line = line.strip()     # Remove the leading spaces and newline character
        line = line.lower()     # Convert the characters in line to lower
        words = line.split(" ") # Split the words of each line
        for word in words:      # Iterate over each word in line
            if word in D:       # Check key words to see if word exists
                D[word] = D[word] + 1      # Increment key value count by 1
            else:
                D[word] = 1     # Create new entry key and assign value to 1
    revSortedDict = dict(sorted(D.items(), key=operator.itemgetter(1),reverse=True)) # Sort dictionary by value in reverse using itemgetter(1) from operator library
    finalDict = itertools.islice(revSortedDict.items(), 0, topNum)  # make a new dictionary by slicing original dictionary and only using 1st maxNum numbers
    return finalDict

def program4():                 # driver for program 4 
    topNum = ''                 # Input number of top n words to apear
    try:
        topNum = int(input('\nEnter a number for the top \'n\' number of words: '))
    except:
        print('Wrong input. Please enter a number ...')
    topN = fileWordOcc(topNum)  # Call file read function passing the n number
    if topN == None:
        print("Error couldn't find file.")
    else:
        for key, value in topN:
            print (key, value)
    print('\nHandled \'Program 4\'')

def timeEfficiency2(funcName):              # Pass function as object 
    def wrapper(*args, **kwargs):           # Defines wrapper it will run the function with its arguements if any
        time1 = time.process_time()         # Calculate initial proccessing time
        funcName(*args, **kwargs)           # Execute function
        time2 = time.process_time()         # Get end time
        print("start: " + str(time1) + " end: " + str(time2) + " time efficiency: " + str((time2-time1))) 
    return wrapper

@timeEfficiency2
def run(aNum):
    listPrimeNumbers(aNum)

def extraCredit():                          # Extra Credit program converting 
    mNum = ''                               # Enter number 
    try:
        mNum = int(input('\nEnter a number for the list of prime numbers: '))
    except:
        print('Wrong input. Please enter a number ...')
    run(mNum)                               # Pass number to decorator function
    print('Handled \'Extra Credit\'')

if __name__=='__main__':         # Main mainu for all programs 
    while(True):
        printMenu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number...')
        if option == 1:
            program1()
        elif option == 2:
            program2()
        elif option == 3:
            program3()
        elif option == 4:
            program4()
        elif option == 5:
            extraCredit()
        elif option == 6:
            print('Exiting...')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 6.\n')
