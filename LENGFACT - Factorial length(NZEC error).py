t=input()
for i in range(t):
    n=input()
    fact=1
    t=0
    for x in range(2,n+1):
        fact*=x
    while fact:
        fact=fact/10
        t+=1
    print t    
        
