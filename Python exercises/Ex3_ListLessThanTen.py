a = [-1, 0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
           
for i in a:
    if i < 5:
        print i,
        
# Extra 2: 
print [i for i in a if i<5]

# extra 1
def extraOne(lst): 
    l = []
    for i in lst:
        if i < 5:
            l.append(i)
    return l

lst = [x for x in a if x < 5]

# Extra 3:
x = raw_input("give a number in list a: ")
print [i for i in a if i < x]

print extraOne(a)


