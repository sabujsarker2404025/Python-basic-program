n=int(input("Entet your number:"))
for i in range (1,n+1,1):
    print(" "*(n-i)+'*'*(2*i-1))
for i in range (n-1,0,-1):
    print(" "*(n-i)+'*'*(2*i-1))
 
  