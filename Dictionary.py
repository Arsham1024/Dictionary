# loading the data from json file
import json
# This is for finding similar words
from difflib import SequenceMatcher

# opening the json file
data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    else:
        return "The word you are looking for does not exist. Double check your word."


def checkword(word):
    ratios = {}
    for key in data:
        ratios[key] = SequenceMatcher(None, word, key).ratio()*100

    # print(f"is the word you are looking for \"{key}\"?")


# Taking the input from the user and turning it to all lower case to
# account for capitalization issues
word = input("What are you looking for? ").lower()
checkword(word)

# output the word to the user
print(translate(word))

