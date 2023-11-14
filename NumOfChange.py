import numpy
 
def minNumOfChangeNaive(denomination, target):
    numOfBC = 0
    strTarget = str(target)
    dec = strTarget[::-1].find('.') # keeps. track of decimal place of the value
    while target != 0: #. while target value hasn't been depleted
        for i in denomination:  # iterate through the denominations
            if target - i >= 0: # check if target value is zero or bigger 
                target -= i # decrement that denomination
                target = round(target, dec) # round target to correct decimal place
                numOfBC += 1    #increment amount of change
                break
    return numOfBC

#https://www.youtube.com/watch?v=8THI_5SViCQ
def minNumOfChangeDP(target, denomination):
    tbl = [float('inf') for x in range(target+1)] # create table and fill it with infinity at the start
    tbl[0] = 0  # change for 0 is 0
    for denom in denomination:  # iterate through each denomination
        for amount in range(len(tbl)):  # iterate through table
            if denom <= amount:     # for each denomination we check if its less or equal to the amount thats in the table
                tbl[amount] = min(tbl[amount], 1 + tbl[amount - denom]) # update tbl element by find minimum change of that amount by subtracting numbers and using remainder + 1
    return tbl[target] if tbl[target] != float('inf') else -1
                
            
deno = [100, 50, 20, 10, 6, 5, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
#deno = [10, 6, 1]
arr1 = [int(num * 100) for num in deno]
arr1 = numpy.asarray(arr1, dtype = 'int')
lengthOfDeno = len(arr1)
#target = 269.63
target = float(input(f"Denominations: {deno}\nEnter the target number (XXXX.XX): "))
intTarget = int(target * 100)
result1 = minNumOfChangeNaive(deno, target)
print(f"Denominations used: {deno}\nTarget: {target}")
print(f"Minimum number of change '(Naive)': {result1}")

print(f"Denominations used: {deno}\nTarget: {target}")
print(f"Minimum number of change '(DP)': {minNumOfChangeDP(intTarget, arr1)}")
