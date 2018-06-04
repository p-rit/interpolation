#to calculate factorial
def fact(x):
	if x==0 or x==1:
		return 1
	else:

		return x*fact(x-1)

#to cal dividend diff table
def f(l1,l2):
	d = [[0 for x in range(len(l1))] for y in range(0,len(l2))]
		
	
	for i in range(0,len(l1)-1):
		for j in range(0,len(l2)-i-1):
			if i==0:
				d[i][j] = (l2[j+1]-l2[j])/(l1[j+1]-l1[j])
			else:
				d[i][j] = (d[i-1][j+1] - d[i-1][j])/(l1[j+1+i] - l1[j])
	return d

print("Enter values of x ")
l1 = [float(x) for x in input().split()]
print("Enter values of y ")	
l2 = [float(x) for x in input().split()]

d = f(l1,l2)
print("enter the x at which u want to know y")
x = float(input())

k= 0 
for i in range(1,len(l2)):# to interpolate
	s = 1
	for j in range(0,i):
		s = s*(x-l1[j])
	
		
	k = k+(s*d[i-1][0])
	
k = k+l2[0]

print(k)

