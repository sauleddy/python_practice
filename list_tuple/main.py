

myList = ['a', 'b', 'c']
print('myList:%s' % myList)
print('len(myList):%d' % len(myList))
myList.append('d')
print('myList after append \'d\':%s' % myList)
myList.insert(1, 'ab')
print('myList after insert \'ab\':%s' % myList)
myList.pop()
print('myList after pop:%s' % myList)
myList.pop(1)
print('myList after pop(1):%s' % myList)

myTuple = (1, [2, 3])
print('myTuple:%s' % (myTuple,))
myTuple[1][0] = 4
print('myTuple after change tuple element:%s' % (myTuple,))
