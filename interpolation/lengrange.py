
#input from user ,values of x and y
print("Enter values of x ")
l1 = [float(x) for x in input().split()]
print("Enter values of y ")	
l2 = [float(x) for x in input().split()]

#interpolation
print("enter value of x at which uwant to know value of y")
x = float(input())
s=0.0
for i in range(len(l1)):
	p=1.0
	for j in range(len(l1)):
		if j!=i :

			p *= (x-l1[j])/(l1[i]-l1[j])
		
	s += p*l2[i]
#displaying result
print(s)		