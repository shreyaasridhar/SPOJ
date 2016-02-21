t=input()
for i in range(t):
    c,k,w=raw_input().split()
    c=int(c)
    k=int(k)
    w=int(w)
    if c*w<=k:
        print "yes"
    else:
        print "no"
