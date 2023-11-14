from time import process_time
import os
import os.path

counter = 0;                # global variale for counter for comparisons

def timeEfficiency(funcName, *args):    # Funtion to print time
    time1 = process_time()         # Calculate initial proccessing time
    count = funcName(*args)             # Execute function
    time2 = process_time()         # Get end time
    print("start: " + str(time1) + " end: " + str(time2) + " time efficiency: " + str((time2-time1))) 

#https://www.geeksforgeeks.org/python-program-for-merge-sort/
def mergeSort(arr, l, r):
    global counter
    if l < r:
        counter += 1
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

def merge(arr, l, m, r):
    global counter
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
    
    
    # Go through both copies until we run out of elements in one
    while i < n1 and j < n2:
        # If our left_copy has the smaller element, put it in the sorted
        # part and then move forward in left_copy (by increasing the pointer)
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        # Opposite from above
        else:
            arr[k] = R[j]
            j += 1
        # Regardless of where we got our element from
        # move forward in the sorted part
        k += 1
        counter += 1
        
    # We ran out of elements either in left_copy or right_copy
    # so we will go through the remaining elements and add them
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted

#https://www.programiz.com/dsa/insertion-sort
def insertionSort(array):
    global counter
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1       
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
            counter += 1
        # Place key at after the element just smaller than it.
        array[j + 1] = key

numList1 = []                                          # create arrays for both sorts
numList2 = []

print("Files in directory: " + str(os.listdir()))      # show file directory
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
        
print("\nFilename: " + str(filename))

print("\nInsertion Sort time in seconds: ")            # sort array1 with insertion sort and call time efficiency function
timeEfficiency(insertionSort, numList1)
print("Number of comparisons: " + str(counter))
counter = 0                                          # reset global counter

print("\nMerge Sort time in seconds: ")                       # sort array1 with merge sort and call time efficiency function
timeEfficiency(mergeSort, numList2, 0, len(numList2) - 1)
print("Number of comparisons: " + str(counter))