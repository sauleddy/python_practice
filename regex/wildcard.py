import re

wildatRegex = re.compile(r'.at')
match = wildatRegex.findall('The cat sat on the floor 1at at')
print(match)

nongreedyRegex = re.compile(r'<.*?>')
match = nongreedyRegex.findall('<This is a book> and a table>')
print(match)
greedyRegex = re.compile(r'<.*>')
match = greedyRegex.findall('<This is a book> and a table>')
print(match)

noNewlineRegex = re.compile('.*')
match = noNewlineRegex.search('abcd efg\nhijk')
print(match.group() + '\n')

newlineRegex = re.compile('.*', re.DOTALL)
match = newlineRegex.search('abcd efg\nhijk')
print(match.group())