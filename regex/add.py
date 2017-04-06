import re

batRegex = re.compile(r'Bat(wo)+man')
match = batRegex.search('The adventure of Batman')
print(match == None)
match = batRegex.search('The adventure of Batwowoman')
print(match.group())