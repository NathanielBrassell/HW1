from bs4 import BeautifulSoup
import re

def findNames(book, content_words):
    #create a dict with key=name; value=occurrences 
    names = {}
    regex = "(?<!\. )[A-Z][a-z]+ ([A-Z][a-z]+ )+"
    for match in re.finditer(regex, book):
        addToDict(match.group(),names)

    # debugging
    print names
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
