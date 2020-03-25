import json
import difflib
from difflib import get_close_matches as gCm

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data.keys():
        return data[word]
    elif word.title() in data.keys():
        return data[word.title()]
    elif word.upper() in data.keys():
        return data[word.upper()]
    elif gCm(word, data.keys(), n = 1, cutoff = 0.8) != []:
        x = input ("Did you mean %s instead? Enter Y if yes, or enter N if not: " % gCm(word, data.keys())[0])
        if x == "Y":
            return translate(gCm(word, data.keys())[0])
        else:
            return ("Please double check then!")
    else:  
        return ("This word doesn't exist")

word = input("Please enter a word: ")

output = translate(word)
if isinstance(output, str):
    print(output)
else:
    for item in output:
        print(item)