

myDict = {'Tom': 100, 'John': 60, 'Mike': 90}
print('myDict:%s' % (myDict,))

print('myDict get(\'John\', -1):%s' % (myDict.get('John', -1),))
print('myDict get(\'John2\', -1):%s' % (myDict.get('John2', -1),))

myDict.pop('John')
print('myDict after pop(\'John\'):%s' % (myDict,))

mySet = set([1, 2, 3, 3])
print('mySet:%s' % (mySet,))
mySet.add(4)
print('mySet after add(4):%s' % (mySet,))
mySet.remove(2)
print('mySet after remove(2):%s' % (mySet,))

mySet1 = set([1, 2, 3])
mySet2 = set([2, 3, 4])
print('mySet1 & mySet2:%s' % (mySet1 & mySet2,))
print('mySet1 | mySet2:%s' % (mySet1 | mySet2,))


