from difflib import get_close_matches

import json

data = json.load(open('data.json'))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        x = get_close_matches(word, data.keys())[0]
        ans = input(f'Did you mean {x} instead? Enter Y if Yes, or N if No.')
        if ans == "Y":
            return data[x]
        elif ans == "N":
            return "Word doesn't exist. Please make sure you spelled it correctly."
        else:
            return "We didn't understand your entry."

    else:
        return "Word doesn't exist. Please double check it."


print("Welcome to Interactive English Dictionary\n")
word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    i = 1
    for item in output:
        print(f"**************{i}***************")
        print(item, "\n")
        i += 1


else:
    print(output)
