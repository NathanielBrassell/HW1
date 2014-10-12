from bs4 import BeautifulSoup
import re


### to consider... ###
# Account for UC (uppercase) words at start of sentence/start of quote,dialogue
# Titles such as: Mr., Ms., Mrs., Dr., Judge, Uncle, Aunt, King, Queen, Captain,
#                 Mister, Miss, Missus, Doctor, Captain, Lady, Lord, etc...
# Implement Miranda's features
# Change sorted dict to list or use list of tuples (string, int)

def findNames(book, content_words):
    #create a dict with key=name; value=occurrences 
    names = {}
    for match in re.finditer("(?<!\. )[A-Z][a-z]+ ([A-Z][a-z]+ )+", book):
        addToDict(match.group(),names)

    # debugging
    print names #debugging
    print "len: %d" % len(names)
    most_common_name= ""
    most_common_count=0;
    for name in names.keys():
        if names[name] > most_common_count and name.lower()[:len(name)-1] not in content_words.lower():
            most_common_name=name
            most_common_count= names[name]
    print most_common_name.lower()
    print content_words.lower()
    return most_common_name

def addToDict(string,dict):
    if string in dict:
        dict[string]+= 1
    else:
        dict[string] = 1;

'''
if __name__=="__main__":
    findNames()
'''
