from random import randint

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for i in a:
    if i in b:
        c.append(i)
print 'c: ', '\t' , c


listA = [randint(1,10) for i in range(1,randint(5,10)) ]
listB = [randint(1,10) for i in range(1,randint(5,10)) ]

print 'listA: ',listA
print 'listB: ' ,listB

d = []
for i in listA:
    if i in listB:
        d.append(i)
print 'd: ','\t', d 

listC = [i for i in listA if i in listB]

print 'listC: ',listC