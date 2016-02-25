x=input()
for ns in range(x):
    i,j=raw_input().split()
    i=int(i)
    j=int(j)
    flag=0
    if abs(j-i)!=2 or i!=j:
        print "No number"
    else:
        if i%2!=0 and j%2!=0:
            print i+j-1
        elif i%2==0 and j%2==0:
            print  i+j     
