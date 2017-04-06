import re

namesRegex = re.compile(r'Agent \w+')
match = namesRegex.sub('CENSORED', 'Agent Alice gave the secret...')
print(match)

namesRegex = re.compile(r'Agent (\w)\w+')
match = namesRegex.sub(r'\1***', 'Agent Alice gave the secret...')
print(match)