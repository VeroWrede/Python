s = raw_input("what string should be tested? ")
l = len(s)
print l
x = 0
y = -1
for x in range(l):
    if s[x] == s[y]:
        x += 1
        y -= 1
    elif s[x] != s[y]:
        print 'not a palindrome'
        break
    elif len(x) == range(l):
        print 'word was: ', '\t', s
        print 'palindrome is: ', '\t', s[::-1]
    else:
        print 'did something happen?'
        break



            
                













