# loading the data from json file
import json
# This is for finding similar words
from difflib import get_close_matches

# opening the json file
data = json.load(open("data.json"))


def translate(word):
    if word in data:
        return data[word]
#     This condition checks for nouns such as paris that are in the dictionary as Paris (title case)
    elif word.title() in data:
        return data[word.title()]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        #     This means that there are close matches found because the list has words in it
        answer =  input("Did you mean %s? Y for yes and N for no: " % get_close_matches(word, data.keys(), cutoff=0.8)[0])
        if answer.lower() == "y":
            return data[get_close_matches(word, data.keys(), cutoff=0.8)[0]]
        elif answer.lower() == "n":
            return "Could not find the word. Try again."
    else:
        return "The word you are looking for does not exist. Double check your word."


while (True):
    # Taking the input from the user and turning it to all lower case to
    # account for capitalization issues
    word = input("\nWhat are you looking for? or Q for quit\n").lower()
    if word == "q":
        print("Goodbye")
        break
    # output the word to the user
    output = translate(word)
    if isinstance(output, list):
        for item in output:
            print(item)
    else:
        print(output)

