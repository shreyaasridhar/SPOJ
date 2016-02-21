def reverse(num):
    return int(str(num)[::-1])
t=input()
for i in range(t):
    i,j=raw_input().split()
    i=int(i)
    j=int(j)
    i=reverse(i)
    j=reverse(j)
    sum=i+j
    print reverse(sum)
