from cProfile import label
import matplotlib.pyplot as plt
from time import process_time
import os
import os.path

def timeEfficiency(funcName, *args):    # Funtion to print time
    time1 = process_time()         # Calculate initial proccessing time
    count = funcName(*args)             # Execute function
    time2 = process_time()         # Get end time
    print("start: " + str(time1) + " end: " + str(time2) + " time efficiency: " + str((time2-time1))) 
    return (time2 - time1)
 
 # reference https://www.geeksforgeeks.org/python-program-for-bubble-sort/
def bubbleSort(arr, low, high):
    n = high
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(low, n + 1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(low, n):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return

# reference https://www.geeksforgeeks.org/quick-sort/
# Function to find the partition position
def partition(array, low, high):
 
    # choose the rightmost element as pivot
    pivot = array[high]
 
    # pointer for greater element
    i = low - 1
 
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
# Function to call the partition function
# and perform quick sort on the array
def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot-1)
        quick_sort(arr, pivot + 1, high)
        return arr
 
# reference https://www.geeksforgeeks.org/advanced-quick-sort-hybrid-algorithm/
# Hybrid function -> Quick + Insertion sort
def bubblesort_quicksort(arr, k, low, high):
    while low < high:
 
        # If the size of the array is less
        # than threshold apply insertion sort
        # and stop recursion
        if high - low <= k:
            bubbleSort(arr, low, high)
            break
 
        else:
            pivot = partition(arr, low, high)
 
            # Optimised quicksort which works on
            # the smaller arrays first
 
            # If the left side of the pivot
            # is less than right, sort left part
            # and move to the right part of the array
            if pivot - low < high - pivot:
                bubblesort_quicksort(arr, k, low, pivot-1)
                low = pivot + 1
            else:
                # If the right side of pivot is less
                # than left, sort right side and
                # move to the left side
                bubblesort_quicksort(arr, k, pivot + 1, high)
                high = pivot - 1
                
a = [ 24, 97, 40, 67, 88, 85, 15,
      66, 53, 44, 26, 48, 16, 52,
      45, 23, 90, 18, 49, 80, 23 ]

b = [ 24, 97, 40, 67, 88, 85, 15,
      66, 53, 44, 26, 48, 16, 52,
      45, 23, 90, 18, 49, 80, 23 ]

print("List before bubble sort: " + str(a))
timeEfficiency(bubbleSort, a, 0, len(a)-1)
print("List after bubble sort: " + str(a))
print("\nList before quicksort: " + str(b))
timeEfficiency(quick_sort, b, 0, len(b)-1)
print("List after quicksort: " + str(b))

numList1 = []                                          # create arrays for both sorts
numList2 = []

print("\nFiles in directory: " + str(os.listdir()))      # show file directory
filename = input("Enter file a file name: ")
check = os.path.exists(filename)                       # check if file exists
if not check:
    print("File not in directory. Exiting...") 
    exit()

text = open(filename, "r")                       # open file and append numbers into arrays
for line in text:                                # Loop through each line of the file
    line = line.split()
    for num in line:                             # Iterate over each number in line
        numList1.append(int(num))
        numList2.append(int(num))
text.close()

try:
    k = int(input("Enter a value for range of k: "))
except ValueError:
    print('The provided value is not an integer')
    exit()

try:
    r = int(input("Enter a value to increment range: "))
except ValueError:
    print('The provided value is not an integer')
    exit()

kvals = []
timey = []

print("\nFilename: " + str(filename))
print("\nQuickSort time in seconds: ")            # sort array1 with insertion sort and call time efficiency function
timeEfficiency(quick_sort, numList1, 0, len(numList1) - 1)
print("\nHybrid QuickSort time in seconds: ")            # sort array1 with insertion sort and call time efficiency function
for i in range(0 , k + 1, r):
    templist = []
    templist = list(numList2)
    kvals.append(i)
    print("k = " + str(i))
    timey.append(timeEfficiency(bubblesort_quicksort, templist, i, 0, len(templist) - 1))
print("\nOptimal k = " + str(kvals[timey.index(min(timey))])  + ": " + str(min(timey)) + " seconds")

print("\nCreating graph...")
plt.plot(kvals, timey, label = "Hybrid Quick Sort", color = "blue")
# naming the x axis
plt.xlabel('List size of k elements')
# naming the y axis
plt.ylabel('Execution time in seconds')
# giving a title to my graph
plt.title('Execution time of combination Ouick Sort and Bubble Sort with k sublists')

plt.legend()

plt.show()


