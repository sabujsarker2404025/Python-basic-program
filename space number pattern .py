n=int(input("Entet your number:"))
for i in range (1,n+1,1):
    for k in range (1,n-i+1,1):
        print(end='  ')
    f=n
    for j in range (1,i+1,1):
        print(f,end=' ')
        f=f-1

    print()  
  