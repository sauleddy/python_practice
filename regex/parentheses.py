import re

"""
search 'Batman' 'Batmobile' 'Batcopter' and 'Batbat'
"""

batregex = re.compile(r'Bat(man|mobile|copter|bat)')
match = batregex.search('Batmobile lost Batcopter a wheel')
print(match.group())
print(match.group(1))






