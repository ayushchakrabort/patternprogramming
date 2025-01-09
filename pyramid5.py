n=int(input("n: "))
for i in range(2*n-1):
    for j in range(1,n+1):
        if j==n or i+j==n or i-j==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()