import math
def small_div(n):
	if n%2==0 and n!=2:
		return False
	else:
		sqrton=math.floor(math.sqrt(n))
		for i in (3,sqrton,2):
			if n % i==0 and n!=3:
				return False
			else:
				if i==sqrton:
					return True
t=input()
for i in range(t):
	x,y=raw_input().split()
	x=int(x)
	y=int(y)
	for n in range(x,y+1):
		if n==2:
			print n
		if small_div(n):
			print n
	print ""	 	
