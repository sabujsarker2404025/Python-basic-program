n=int(input("Entet your number:"))
for i in range (n,0,-1):
    for k in range (1,n-i+1,1):
        print(end='  ')
    f=n
    for j in range (1,i+1,1):
        if (f%2==0):
            print(0,end=' ')
        else:
            print(1,end=' ')    
        f=f-1

    print()  
  