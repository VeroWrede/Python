from random import randint

lstOne = [ randint(0,20) for i in range(15)]
lstTwo = [ randint(0,20) for i in range(15)]
lstThree = []

lst = set()

lstThree = [i for i in lstOne if i in lstTwo]
lstThree = set(lstThree)
lstThree = list(lstThree)
print 'lstOne: ', lstOne
print 'lstTwo: ', lstTwo
print 'set: ','\t', lstThree