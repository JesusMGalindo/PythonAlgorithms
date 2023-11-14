'''
Visits "https://covid19.colorado.gov/data" site and pull out the case summary snapshot tabel and puts it into a table in html
Scrapes the case summary snapshot table from "https://covid19.colorado.gov/data" and puts infor into a html table
'''

from bs4 import BeautifulSoup
import requests
import pandas

url = requests.get("https://covid19.colorado.gov/data") # make a request to a web page, and return the status code:
soup = BeautifulSoup(url.content, 'html5lib') # parse html code with beatiful soup
scripts = soup.find_all(attrs={"dir":"ltr"}) # filter out the html from right to left direction

counter = 0
arr = [] # list for uppending each key value pair of table
for script in soup.find_all("table"): # filter tables
    counter += 1          # desired table is thec first table of the html code
    if(counter > 1):
        break
    for nty in script.find_all("td"):  # iterate all table info
        entry = nty.text
        arr.append(entry)   # append each table entry

res = [arr[i:i+2] for i in range(0, len(arr), 2)] # group list into group of two sublists grouping keys with values
df = pandas.DataFrame({0:res[0], 1:res[1], 2:res[2], 3:res[3], 4:res[4], 5:res[5], 6:res[6], 7:res[7]}) # make into data fram matrix
print(df)
textfile = open("Extra_Credit2.html", "w")  # convert and write into html code to file
file = df.to_html()
textfile.write(file)
textfile.close()
