import re

string = input()
upper = len(re.findall("[A-Z]", string))
lower = len(re.findall("[a-z]", string))

print(string.upper() if upper > lower else string.lower())