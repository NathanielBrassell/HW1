import re, google, urllib, Where
from bs4 import BeautifulSoup, SoupStrainer


def addToDict(string,dict):
    if string in dict:
        dict[string]+= 1
    else:
        dict[string] = 1;

def findMostCommon(dict, content):
    most_common_key = ""
    most_common_count = 0;
    for key in dict.keys():
        if dict[key] > most_common_count and key.lower()[:len(key)-1] not in content.lower():
            most_common_key = key
            most_common_count = dict[key]
    #print most_common_name.lower()
    #print content_words.lower()
    return most_common_key

def findNames(text, content):
    #create a dict with key=name; value=occurrences 
    names = {}
    regex = "(?<!\. )[A-Z][a-z]+ ([A-Z][a-z]+ )+"
    for match in re.finditer(regex, text):
        addToDict(match.group(),names)
    return findMostCommon(names, content)

def findDates(text, content):
    dates = {}
    regex = "(January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{1,4}( BC| C.E.| A.D.| B.C.)?"
    for match in re.finditer(regex, text):
        addToDict(match.group(),dates)
    return findMostCommon(dates, content)

def search_query(question):
    question_word= (question.split(" ")[0]).lower()
    content_words=" ".join(question.split(" ")[1:])
    g= google.search(content_words, num=20, stop=20)
    search_results=""
    only_p= SoupStrainer("p")

    for result in g:
        search_results += BeautifulSoup(urllib.urlopen(result),parse_only=only_p).get_text()
        #print search_results

    response=""
    if question_word == "who":
        response = findNames(search_results,content_words)
    elif question_word == "where":
        response = Where.where(search_results, content_words)
    elif question_word == "when":
        response = findDates(search_results,content_words)
    return response
