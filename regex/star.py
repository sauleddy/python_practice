import re

batRegex = re.compile(r'Bat(wo)*man')
match = batRegex.search('The adventure of Batman')
print(match.group())
match = batRegex.search('The adventure of Batwowowowoman')
print(match.group())