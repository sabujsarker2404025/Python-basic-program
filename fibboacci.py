n = int(input("Enter a number: "))
a,b,ct=0,1,0

while ct<n:
     print(a,end=" ")
     a,b=b,a+b
     ct=ct+1