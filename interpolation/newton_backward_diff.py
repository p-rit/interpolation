#to calculate factorial
def fact(x):
	if x==0 or x==1:
		return 1
	else:
		return x*fact(x-1)

#to calculate diff table 
def f(l1,l2):
	d = [[0 for x in range(len(l1))] for y in range(0,len(l2))]
		
	
	for i in range(0,len(l1)-1):
		for j in range(0,len(l2)-i-1):
			if i==0:
				d[i][j] = l2[j+1]-l2[j]
			else:
				d[i][j] = d[i-1][j+1] - d[i-1][j]
	return d

print("Enter values of x ") 
l1 = [float(x) for x in input().split()]
print("Enter values of y ")	
l2 = [float(x) for x in input().split()]

d = f(l1,l2) #diff table in d 

print("enter the x at which u want to know y")
x = float(input())
for i in range(len(l1)): #to cal no just greater thn x
	if(l1[i]>x):
		x0 = l1[i]
u = (x-x0)/(l1[1]-l1[0])

k= 0 
for i in range(1,len(l2)): # to interpolate
	s = 1
	for j in range(0,i):
		s = s*(u+j)
	
		
	k = k+(s*d[i-1][len(l2)-i-1])/fact(i)
	
k = k+l2[-1]

print(k)

