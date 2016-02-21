import math
t=input()
for x in range(t):
    i,j=raw_input().split()
    i=int(i)
    j=int(j)
    for n in range(i,j+1):
        prime = True
        for i in range(2,int(math.sqrt(n))+1):
        	if (n%i==0):
        		prime = False
        if prime and n!=1:
        	print n
    print ""        
