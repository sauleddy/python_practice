import re

greedyRegex = re.compile(r'(Ha){2,4}')
match = greedyRegex.search('HaHaHaHa')
print(match.group())

nongreedyRegex = re.compile(r'(Ha){2,4}?')
match = nongreedyRegex.search('HaHaHaHa')
print(match.group())