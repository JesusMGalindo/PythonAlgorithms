from bs4 import BeautifulSoup
import json
import requests

headers = {'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.3'}

url = requests.get("http://www.ucdenver.edu/pages/ucdwelcomepage.aspx")  # make a request to a web page, and return the status code:
soup = BeautifulSoup(url.content, 'html5lib')   # parse html code with beatiful soup
scripts = soup.find_all(attrs={"type":"application/ld+json"})   # filter out the html for the json part
scripts = [script for script in scripts]  # get application script and its scripts inside

for script in list(scripts): # iterate through each script
  links = script.contents[0] # set links to the first index
  j = json.loads(links) # retreive the JSON string object and converts it into a python dictionary
  counter = 0 # start counter to get only first 10
  for department in j["department"]: # for each department in the dictionary
    counter += 1 
    if(counter > 10): # end loop once count = 10
        break
    else:
        print(str(counter) + ".", department["name"] + " -", department["url"]) #from department, get the name and url only

file = json.dumps(j, indent=4) #Dump dictionary to JSON dump
textfile = open("Extra_Credit1.json", "w")
textfile.write(file)
textfile.close()