import re, google, urllib

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

def where(google_results, content):
    locations=["street","alley","avenue","place","st","drive","ave","manor","house","school","tower","building","road","city","state","nation"]
    regex="((\d{1,4}\w?) [A-Z]\w+ ([A-Z]\S+ )+)"
    results = re.findall(regex,google_results)
    answers={}
    print results
    for result in results:
        loc=False;
        for word in result[0].split(" "):
            if word.lower() in locations:
                loc=True
        if loc:
            addToDict(result[0],answers)
    print answers
    return findMostCommon(answers,content)

