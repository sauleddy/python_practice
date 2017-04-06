import re

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
match = phoneRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(match)

phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
match = phoneRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(match)