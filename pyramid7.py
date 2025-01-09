n=int(input("n: "))
for i in range(2*n-1):
    for j in range(n):
        if j==0 or i==j or i+j==2*n-2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

''' *     
    * *
    *   *
    * *
    *     '''