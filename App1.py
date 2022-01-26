import json
from difflib import get_close_matches

#Opening the JSON file
datas = json.load(open("data.json")) 

def trans(w):
    w = w.lower()                           #converting the words to the lower case
    if w in datas:
        return datas[w]
    elif w.title() in datas:                #converting the words if the user enter "delhi" it will also check for "Delhi"
        return datas[w.title()]
    elif w.upper() in datas:                #in case user enters words in USA or NATO
        return datas[w.upper()]
    elif len(get_close_matches(w, datas.keys())) > 0:
        yn= input("Did you mean %s instead? Enter Y for Yes or N for No: " %get_close_matches(w, datas.keys())[0]) #getting the close match for the incorrect word
        if yn == "Y":
            return datas[get_close_matches(w, datas.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please check the word"
        else:
            return "Please enter the correct entry."
    else:
        return "The word doesn't exist. Please check the word"

word = input("Enter the word:")             #Getting the input

output = trans(word)

if type(output) == list:                    #printing the list in new lines
    for item in output:
        print(item)
else:
    print(output)