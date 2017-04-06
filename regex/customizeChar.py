import re

vowelRegex = re.compile(r'[aeiouAEIOU]')
match = vowelRegex.findall('Robocop eats baby');
print(match)
