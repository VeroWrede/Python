n = raw_input("write a number: ")

def fib(x):
    print "hello"
    f1 = 1
    f2 = 1
    if x == 1:
        return f1
    if x ==2:
        return f2
    
    i = 3
    fibNMinusOne = f2
    fibNMinusTwo = f1
    fibI = 0 # just initializing, this value is never used
    while i<=x:
        fibI = fibNMinusOne + fibNMinusTwo
        fibNMinusTwo = fibNMinusOne
        fibNMinusOne = fibI
        if i == x:
            return fibI
        i += 1  
        

def recursiveFib(n):
    if n == 1 or n == 2:
        return 1
    else:
         return recursiveFib(n - 1) + recursiveFib(n - 2)

map = {}
def dynamicFib(n):
    if n == 1 or n == 2:
        return 1
    elif n in map:
        return map[n]
    else:
        fibN = dynamicFib(n - 1) + dynamicFib(n - 2)
        map[n] = fibN
        return fibN

print fib(int(n))
print recursiveFib(int(n))
print dynamicFib(int(n))


def nthfib(x):
    print "with list"
    arr = [0] * (x + 1)
    arr[1] = 1
    if x == 1:
        return arr
    arr[2] = 1
    if x == 2:
        return arr
    i = 3
    while i<=x:
        arr[i] = arr[i-1] + arr[i-2]
        if i == x:
            return arr
        i += 1
     

print nthfib(int(n))


