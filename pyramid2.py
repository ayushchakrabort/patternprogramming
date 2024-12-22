n=int(input("n: "))
for i in range(n):
    for j in range(2*n-1):
        if i==j  or i+j==2*n-2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

'''*               * 
     *           *
       *       *
        *   *
          *           '''