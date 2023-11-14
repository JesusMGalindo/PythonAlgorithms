'''
Jesus Galindo
11/4/2022
CSCI 3412
Professor: Sung-Hee Nam
'''

from time import process_time
import os
import os.path
import heapq
import itertools

def timeEfficiency(funcName, *args):    # Funtion to print time
    time1 = process_time()         # Calculate initial proccessing time
    funcName(*args)             # Execute function
    time2 = process_time()         # Get end time
    print("start: " + str(time1) + " end: " + str(time2) + " time efficiency: " + str((time2-time1))) 
    return (time2 - time1)

#https://www.geeksforgeeks.org/radix-sort/
# Python program for implementation of Radix Sort
# A function to do counting sort of arr[] according to
# the digit represented by exp.
def countingSort(arr, exp1):
 
    n = len(arr)
 
    # The output array elements that will have sorted arr
    output = [0] * (n)
 
    # initialize count array as 0
    count = [0] * (10)
 
    # Store count of occurrences in count[]
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1
 
    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]
 
    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
 
    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]
 
 #https://www.geeksforgeeks.org/radix-sort/
# Method to do Radix Sort
def radixSort(arr):
 
    # Find the maximum number to know number of digits
    max1 = max(arr)
 
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp >= 1:
        countingSort(arr, exp)
        exp *= 10

#https://www.scaler.com/topics/data-structures/bucket-sort/
def bucketSorting(array, noOfBuckets):
    maxElement = max(array)
    minElement = min(array)

    # Calculate Range
    Range = (maxElement - minElement) / noOfBuckets

    temp = []

    # create n(noOfBuckets) empty buckets
    for i in range(noOfBuckets):
        temp.append([])

    # Insert elments of array in corresponding buckets
    for i in range(len(array)):
        diff = (array[i] - minElement) / Range - int((array[i] - minElement) / Range)

        if(diff == 0 and array[i] != minElement):
            temp[int((array[i] - minElement) / Range) - 1].append(array[i])

        else:
            temp[int((array[i] - minElement) / Range)].append(array[i])

    # Sort the buckets individually
    for i in range(len(temp)):
        if len(temp[i]) != 0:
            temp[i].sort()

    # Gather elements from all the buckets to get sorted array
    k = 0
    for lst in temp:
        if lst:
            for i in lst:
                array[k] = i
                k = k+1

def mergeKSortedLists(lists):
    heap = []
    for i, row in enumerate(lists):  # for each index i and row of lists[i]
        if row:                      # if row is non empty
            heapq.heappush(heap, (row[0], i, 0))  # insert (row[0], i, 0) into heap for initial heap
    res = []                           # result list for a new sorted list
    while heap:                        # while heap is not empty
        num, row, col = heapq.heappop(heap)  # num, row, col := top element of heap
        res.append(num)                    # insert num at the end of res
        if col < len(lists[row]) - 1:      # if col < size of lists[row] - 1 to check if there are values in sublist to add
            heapq.heappush(heap, (lists[row][col + 1], row, col + 1))  # insert lists[row, col + 1], row, col + 1 into heap
    return res

def SortKLists(lst, lenOfList):
    res = [lst[i:i+lenOfList] for i in range(0, len(lst), lenOfList)] # spilt list into sublists and store them into res array for 2d array
    mid = int(len(lst)/2)                         # get middle of array
    for lst in itertools.islice(res, mid):        # iterate through two havles of the array and sort both halves using two different sorts
        radixSort(lst)
    for lst in itertools.islice(res, mid, len(res)):
        bucketSorting(lst, 5)
    return res

def linearMergeKSortedLists(lst):
    result = []
    isLoop = True
    while(isLoop):
        smallest = 10000000000000
        index = 0
        for i, sublst in enumerate(lst): # looks through each sublist and keeps track of index of sublist runs o(k)
            if len(sublst) == 0:           # skips empty lists
                continue
            if sublst[0] < smallest and len(sublst) > 0:  # finds min of each array until all empty and looks through each value runs O(n)
                smallest = sublst[0]
                index = i
        result.append(lst[index].pop(0))  # append min to result array and pop off that value two its corresponding array
        if not any(lst):  # checks is list is empty after popping all used elements
            isLoop = False   # ends loop and returns result array
    return result
#------------------------------------------------------ Driver

testlist1 = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
testlist1 = SortKLists(testlist1, 4)
testlist2 = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
testlist2 = SortKLists(testlist2, 4)
print("Testlist 1 before min-heap merge: ", testlist1)
print("Testlist 1 after min-heap merge: ", mergeKSortedLists(testlist1))
print("\nTestlist 2 before linear merge: ", testlist2)
print("Testlist 2 after linear merge: ", mergeKSortedLists(testlist2))

numList1 = []                                       # create arrays for both sorts
numList2 = []

print("\nSelect a file to test both merge alogorithms.\nFiles in directory: " + str(os.listdir()))   # show file directory
filename = input("Enter file a file name: ")        # check if file exists
if not (os.path.exists(filename)):
    print("File not in directory. Exiting...") 
    exit()

text = open(filename, "r")                       # open file and append numbers into arrays
for line in text:                                # Loop through each line of the file
    line = line.split()
    for num in line:                             # Iterate over each number in line
        numList1.append(int(num))
        numList2.append(int(num))
text.close()

sortedlist1 = SortKLists(numList1, 10000)        # split and sortk each individual sublist
sortedlist2 = SortKLists(numList2, 10000)
print("\nMin-heap merge time efficiency: ")      # find out how long it took to merge using both algorithms
heapTime = timeEfficiency(mergeKSortedLists, sortedlist1)
print("\nLinear-merge time efficiency: ")
linearTime = timeEfficiency(linearMergeKSortedLists, sortedlist2)

if(heapTime > linearTime):
    print("\nLinear O(nk) method is faster by: ", heapTime-linearTime, "seconds")
if(heapTime < linearTime):
    print("\nMin-heap O(nlogk) method is faster by: ", linearTime-heapTime, "seconds")
