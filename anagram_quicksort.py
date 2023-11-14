'''
Given two strings s1 and s2, check if both strings are anagrams of each other.
'''

def checkAnagram(string1, string2):  # function to check anagrams
    list1 = []                          # put characters in string into arrays
    # clean strings first by removing spaces and converting to lower
    list2 = []
    string1 = string1.replace(" ", "")
    string2 = string2.replace(" ", "")
    string1 = string1.lower()
    string2 = string2.lower()
    for ch in string1:
        list1.append(ch)
    for ch in string2:
        list2.append(ch)
    list1 = quickSort(list1, 0, len(list1)-1)  # sort arrays via quicksort
    list2 = quickSort(list2, 0, len(list2)-1)
    if (list1 == list2):
        print("True.")               # Compare sorted arrays to see if anagrams
    else:
        print("False.")


def quickSort(array, left, right):   # quicksort function to sort an array
    # If array only has one value return array or when halves reach their smallest point
    if len(array) == 1:
        return array
    if left < right:                          # Divide array in half and sort recursivly based of the pivot index we recieve from partitioning over and over
        pivotIndex = partition(array, left, right)
        quickSort(array, left, pivotIndex-1)       # Sort left
        quickSort(array, pivotIndex+1, right)      # sort right
    return array


# function to semi sort array by swapping elements relative to pivot
def partition(array, left, right):
    pivot, countIndex = array[right], left
    # We go up the array comparing elements and swapping them relative to pivot
    for i in range(left, right):
        if array[i] <= pivot:        # If the i'th postion is smaller we swap the bigger elements to the right by swapping with the countIndex
            array[i], array[countIndex] = array[countIndex], array[i]
            countIndex += 1
    array[countIndex], array[right] = array[right], array[countIndex]
    # once the array is semisorted we will get the index index value of the pivot in the sorted array
    return countIndex


cont = True                          # Main driver to recieve inputed strings
while cont == True:
    print("Enter two strings.\n")
    s1 = input("First string: ")
    s2 = input("Second string: ")
    checkAnagram(s1, s2)
    choice = input("\nDo you want to enter another two string? Y/N, Yes/No?")
    if ((choice.lower() == "yes") | (choice.lower() == 'y')):
        print("\n")
        continue
    else:
        choice = False
        break
