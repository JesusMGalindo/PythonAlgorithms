from time import process_time
import os
import os.path

def timeEfficiency(funcName, *args):    # Funtion to print time
    time1 = process_time()         # Calculate initial proccessing time
    funcName(*args)             # Execute function
    time2 = process_time()         # Get end time
    print("start: " + str(time1) + " end: " + str(time2) + " time efficiency: " + str((time2-time1))) 
    return (time2 - time1)

def max_heapify_itr(array, i):
    loop = True
    while loop:
        l = 2 * i
        r = 2 * i + 1 
        length = len(array) - 1
        largest = i
        
        # If left child is larger than root
        if l <= length and array[i] < array[l]:
            largest = l
        else:
            largest = i
        # If right child is larger than largest so far
        if r <= length and array[largest] < array[r]:
            largest = r
        # If largest is not root
        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            i = largest
        else:
            loop = False
    return array

def max_heapify_rec(array, i):
      left = 2 * i
      right = 2 * i + 1
      length = len(array) - 1  # for termination condition check
      largest = i

      if left <= length and array[i] < array[left]:
          largest = left
      if right <= length and array[largest] < array[right]:
          largest = right
      if largest != i:
          array[i], array[largest] = array[largest], array[i]
          max_heapify_rec(array, largest)
      return array

def buildMaxHeap_rec(arr):
    # Index of last non-leaf node
    o = int((len(arr) - 1) / 2)
    
    # Perform reverse level order traversal
    # from last non-leaf node and heapify
    # each node
    for i in range(o, -1, -1):
        max_heapify_rec(arr, i)
    return arr

def buildMaxHeap_itr(arr):
    # Index of last non-leaf node
    o = int((len(arr) - 1) / 2)
    
    # Perform reverse level order traversal
    # from last non-leaf node and heapify
    # each node
    for i in range(o, -1, -1):
        max_heapify_itr(arr, i)
    return arr

    
testlist1 = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]     # test the heapify functions via build max heap
testlist2 = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
print("Testlist 1 before recursive heapify: ", testlist1)
print("Testlist 1 after recursive heapify: ", buildMaxHeap_rec(testlist1))
print("\nTestlist 2 before iterative heapify: ", testlist2)
print("Testlist 2 after iterative heapify: ", buildMaxHeap_itr(testlist2))

arr = []
arr2 = []

print("\nSelect a file to test both heapify alogorithms.\nFiles in directory: " + str(os.listdir()))   # show file directory
filename = input("Enter file a file name: ")        # check if file exists
if not (os.path.exists(filename)):
    print("File not in directory. Exiting...") 
    exit()

text = open(filename, "r")                       # open file and append numbers into arrays
for line in text:                                # Loop through each line of the file
    line = line.split()
    for num in line:                             # Iterate over each number in line
        arr.append(int(num))
        arr2.append(int(num))
text.close()
 
print("\nRecursive heapify time complexity: ")  # test both algorithms with the two arrays
rec_time = timeEfficiency(buildMaxHeap_rec, arr)
print("\nIterative heapify time complexity: ")
itr_time = timeEfficiency(buildMaxHeap_itr, arr2)

if(rec_time > itr_time):
    print("\nIterative method is faster by: ", rec_time-itr_time, "seconds")
if(rec_time < itr_time):
    print("\nRecursive method is faster by: ", itr_time-rec_time, "seconds")