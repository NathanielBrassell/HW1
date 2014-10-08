from bs4 import BeautifulSoup
import re


### to consider... ###
# Account for UC (uppercase) words at start of sentence/start of quote,dialogue
# Titles such as: Mr., Ms., Mrs., Dr., Judge, Uncle, Aunt, King, Queen, Captain,
#                 Mister, Miss, Missus, Doctor, Captain, Lady, Lord, etc...
# Implement Miranda's features
# Change sorted dict to list or use list of tuples (string, int)

def findNames():
    #create a dict with key=name; value=occurrences 
    names = {}
    for match in re.finditer("(?<!\. )[A-Z][a-z]+ [A-Z][a-z]+", book):
        addToDict(match.group(),names)

    # debugging
    print names #debugging
    print "len: %d" % len(names)

def addToDict(string,dict):
    if string in dict:
        dict[string]+= 1
    else:
        dict[string] = 1;


if __name__=="__main__":
    findNames()
