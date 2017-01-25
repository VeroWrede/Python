from random import randint

lstOne = [ randint(0,20) for i in range(15)]
lstTwo = [ randint(0,20) for i in range(15)]
lstThree = []

#lstThree = [ i for i in lstOne if not i in lstThree and i in lstTwo]  why does and if not not work here?
lstThree = [ i for i in lstOne if i in lstTwo and if not i in lstThree]

lst = [i for i in lstOne if i in lstTwo]
for i in lst:
    if not i in lstThree:
        lstThree.append(i)
    elif i in lstThree:
        lst.pop(i)
    else:
        print "welcome to the else section"

print 'lstOne: ', lstOne
print 'lstTwo: ', lstTwo
print 'lstThree: ', lstThree