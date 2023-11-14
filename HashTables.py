import os
import os.path
import numpy
from plotly.graph_objs import Bar, Layout
from plotly import offline
import plotly
import collections

global count 

def editDistance(str1, str2, m, n):     # use the global variable count to count recursions
    global count   # bookkeeping purpose
    count += 1
    # If empty, return the length of the other string
    if m == 0 : return n 
    if n == 0 : return m
    if str1[m-1]== str2[n-1]: 
        return editDistance(str1, str2, m-1, n-1)
    return 1 + min(editDistance(str1, str2, m, n-1),
        editDistance(str1, str2, m-1, n),
        editDistance(str1, str2, m-1, n-1))
    
tbl = {}
tbl2 = {}
str1 = "012345678"
colisions = 0
colisions2 = 0
numList1 = []                                       # create arrays for both sorts

print("\nSelect a file to create a hash table.\nFiles in directory: " + str(os.listdir()))   # show file directory
filename = input("Enter file a file name: ")        # check if file exists
if not (os.path.exists(filename)):
    print("File not in directory. Exiting...") 
    exit()

text = open(filename, "r")                       # open file and append numbers into arrays
for line in text:                                # Loop through each line of the file
    line = line.split()
    for num in line:                             # Iterate over each number in line
        numList1.append(num)                     # append each number as a string to list
text.close()

for string in numList1:                 # iterate over each string number
    count = 0                           # reset count to 0
    editDistance(string, str1, len(string), len(str1))      # Call edit distance to get new count
    hashf = numpy.floor(10000 * ((count * 0.6180339) % 1))  # Make a hash index for the second table to compress the slots to 10000
    if count in tbl:                # fill in table 1 using count variable by checking if it exists otherwise increment colision
        colisions += 1
        tbl[count] += 1
    else:
        tbl[count] = 0 
    if hashf in tbl2:               # fill in table 2 using hashf variable by checking if it exists otherwise increment colision
        colisions2 += 1
        tbl2[hashf] += 1
    else:
        tbl2[hashf] = 0 

print("Table 1 total colsions:", colisions)     # display total colisions
print("Table 2 total colsions:", colisions2)
print("Graphing...")


ordered = collections.OrderedDict(sorted(tbl.items())) # sort the two tables for display purposes
ordered2 = collections.OrderedDict(sorted(tbl2.items())) 
axis1 = Bar(x=list(ordered.keys()),y= list(ordered.values()))
axis2 = Bar(x=list(ordered2.keys()),y= list(ordered2.values()))

plotly.offline.plot({                  # plot table 1
                        "data": [ axis1 ], 
                        "layout": Layout(title="<b>Edit Distance Hash Regular</b>", 
                                            xaxis= dict(
                                                title= '<b>Hash Keys</b>',
                                                zeroline= False,
                                                showline=True
                                            ),
                                            yaxis=dict(
                                                title= '<b>Collision Size per Bucket</b>',
                                                zeroline=False,
                                                showline=True
                                            ),
                                            font=dict(
                                                family='Courier New, monospace', 
                                                size=12, 
                                                color='rgb(0,0,0)'
                                            ),
                                            paper_bgcolor='rgb(255,255, 255)',
                                            plot_bgcolor='rgb(255,255,255)'
                                        )
                    }, filename="test1.html")

plotly.offline.plot({              # plot table 2
                        "data": [ axis2 ], 
                        "layout": Layout(title="<b>Edit Distance Hash Uniformity</b>", 
                                            xaxis= dict(
                                                title= '<b>Hash Keys</b>',
                                                zeroline= False,
                                                showline=True
                                            ),
                                            yaxis=dict(
                                                title= '<b>Collision Size per Bucket</b>',
                                                zeroline=False,
                                                showline=True
                                            ),
                                            font=dict(
                                                family='Courier New, monospace', 
                                                size=12, 
                                                color='rgb(0,0,0)'
                                            ),
                                            paper_bgcolor='rgb(255,255, 255)',
                                            plot_bgcolor='rgb(255,255,255)'
                                        )
                    }, filename="test2.html")
print("Finished")
