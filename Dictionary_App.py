'''
There can be 3 scenarios:
1. User input results in an exact match: Meaning of the input is displayed as output.
2. User input contains a typo: Closest matching word is suggested.
3. User input is a junk value: Error message is displayed.
'''
import json
import time
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
	word = word.lower()												# Makes the program case-insensitive. Data in json file in lower case.
	if word in data:
		return data[word]
	elif word.title() in data: 											# If user entered "texas" this will check for "Texas" as well.
		return data[word.title()]
	elif word.upper() in data: 											# In case user enters words like USA or NATO
		return data[word.upper()]
	elif len(get_close_matches(word, data.keys())) > 0:
		yn = input("Did you mean %s instead? Enter Y if YES or N if NO: " % get_close_matches(word, data.keys())[0]) # First element of the close matches
		if yn.lower() == "y":
			return data[get_close_matches(word, data.keys())[0]]
		elif yn.lower() == "n":
			return "The word doesn't exist. Please double check it."
		else:
			return "Invalid entry!"
	else:
		return "The word doesn't exist. Please double check it."


while True:
	word = input("Enter a word or type esc to exit: ")

	if word == 'esc':
		print("Thank You!")
		time.sleep(2)
		break
		SystemExit()

	else:
		output = translate(word)
		if type(output) == list:
			for item in output:
				print(item)
		else:
			print(output)
