import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
SequenceMatcher(None, "rainn", "rain").ratio()
data = json.load(open('data.json'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())):
        yn = input("Did you mean %s instead?  Y/N " % get_close_matches(word, data.keys())[0])
        if yn == "Y" or yn == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N" or yn == "n":
            return "The word does not exist, try again"
            print(translate(word))
        else:
            return "Invalid request, try again"
    else:
        return "The word does not exist, try again"

def translator():
    word = input("Enter word: ")
    output = translate(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)

    choice = input("Find another word? Y/N")
    if choice == "Y" or choice == "y":
        translator()
    elif choice == "N" or choice == "n":
        print("Goodbye")
    else:
        print("Invalid command, goodbye")

translator()