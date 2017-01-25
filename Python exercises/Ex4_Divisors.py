n = raw_input("who's devisors would you like to see? ")

v = int(n)
for i in range(1, v):
    if v % i == 0:
        print i 



