from random import randint

listA = [randint(1,15) for i in range(1,randint(5,15)) ]

listB = [i for i in listA if i%2 == 0]
print 'listA: ', listA
print 'evens: ', listB