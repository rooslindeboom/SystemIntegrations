# Written: Roos Lindeboom 30 aug 2022

import json

# --- TXT ---
# Read file text
print("-- TXT --\n")
with open('Assignment-1-File formats/Article files/Articles/Article.txt') as f:
    contents = f.read()
    print(contents)


# --- XML ---
print("-- XML --\n")

# Read file XML
from xml.dom import minidom

# parse an xml file by name
file = minidom.parse('Assignment-1-File formats/Article files/Articles/Article.xml')

#use getElementsByTagName() to get tag
article = file.getElementsByTagName('article')


for elem in article:
  print(elem.firstChild.data)


# --- JSON ---
print("-- JSON --\n")
# Opening JSON file
f = open('Assignment-1-File formats/Article files/Articles/Article.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
print(data['article'])
  
# Closing file
f.close()
