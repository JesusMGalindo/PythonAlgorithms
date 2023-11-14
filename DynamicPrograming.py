'''
Function will test three edit distance functions naive recursive, memoization, and bottom up iterative. It will compare each string in a file with the string "012345678". It will display the time complexities of all three comparing their run times.
Takes user input for a filename in the directory and compares each number as a string to the string "012345678" via edit distance and compare run times.
'''

from time import process_time
import os
import os.path

global count

def timeEfficiency(funcName, *args):    # Funtion to print time
    time1 = process_time()         # Calculate initial proccessing time
    funcName(*args)                # Execute function
    time2 = process_time()         # Get end time
    print("start: " + str(time1) + " end: " + str(time2) + " time efficiency: " + str((time2-time1))) 
    return (time2 - time1)

def editDistance(str1, str2, m, n):
    #global count   # bookkeeping purpose
    ##count += 1
    # If empty, return the length of the other string
    if m == 0 : return n 
    if n == 0 : return m
    if str1[m-1]== str2[n-1]: 
        return editDistance(str1, str2, m-1, n-1)
    return 1 + min(editDistance(str1, str2, m, n-1),
        editDistance(str1, str2, m-1, n),
        editDistance(str1, str2, m-1, n-1))
    
def editDistanceDP(s1, s2, m, n, memo):
    #global count
    #count += 1
    if memo[m][n] > -1: return memo[m][n]
    if m == 0 : memo[m][n] = n; return memo[m][n]
    if n == 0 : memo[m][n] = m; return memo[m][n]
    if s1[m-1] == s2[n-1] : 
        memo[m][n] = editDistanceDP(s1, s2, m-1, n-1, memo)
        return memo[m][n]
    memo[m][n] = 1 + min(editDistanceDP(s1, s2, m, n-1, memo),
        editDistanceDP(s1, s2, m-1, n, memo),
        editDistanceDP(s1, s2, m-1, n-1,memo))
    return memo[m][n]

def edit_distance(s1, s2):
    m = len(s1)+1
    n = len(s2)+1
    tbl = {}
    for i in range(m): tbl[i,0]=i   #initialization
    for j in range(n): tbl[0,j]=j   #initialization
    
    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if s1[i-1] == s2[j-1] else 1 # the same or not (replacement)
            tbl[i,j] = min(tbl[i, j-1]+1, tbl[i-1, j]+1, tbl[i-1, j-1]+cost)
    return tbl[i,j]

def naive(list, str):
    dis = 0
    for string in list:
        dis = editDistance(string, str, len(string), len(str))
    return

def DP(list, str):
    dis = 0
    for string in list:
        tbl = [[-1 for i in range(len(str)+1)]   for j in range(len(string)+1)]
        for i in range(len(string)): tbl[i][0]=i # first column initialization (Source is empty string)
        for j in range(len(str)): tbl[0][j]=j  # first row initialization (Target is empty string) 
        dis = editDistanceDP(string, str, len(string), len(str), tbl)
    return

def bottom_up(list, str):
    dis = 0
    for string in list:
        dis = edit_distance(string, str)
    return

#------------------------------------------------------ Driver
count = 0

str1 = "012345678"

numList1 = []                                       # create arrays for both sorts

print("\nSelect a file to test edit distance alogorithms.\nFiles in directory: " + str(os.listdir()))   # show file directory
filename = input("Enter file a file name: ")        # check if file exists
if not (os.path.exists(filename)):
    print("File not in directory. Exiting...") 
    exit()

text = open(filename, "r")                       # open file and append numbers into arrays
for line in text:                                # Loop through each line of the file
    line = line.split()
    for num in line:                             # Iterate over each number in line
        numList1.append(num)
text.close()

print("Calculating...")                     # call tim efficiancy functions for each function method
timeEfficiency(naive, numList1, str1)
timeEfficiency(DP, numList1, str1)
timeEfficiency(bottom_up, numList1, str1)
