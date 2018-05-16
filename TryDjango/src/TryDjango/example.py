'''
Created on May 12, 2018

@author: sneha
'''
import re

try:
    f=open("first.txt",'w')
    f.write("My second line")
except IOError:
    print("Error") 
f.close()

patterns = ["term1", "term2"]

text="this is the string with term1"

for pattern in patterns:
    print("I am looking for:"+pattern)
    if re.search(pattern,text):
        print("MATCH")
    else:
        print("No Match")