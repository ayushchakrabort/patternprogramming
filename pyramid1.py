n=int(input("n: "))
for i in range(n):
    for j in range(2*n-1):
        if i+j==n-1 or j-i==n-1 or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


'''         *
          *   *
        *       *
      *           *
    * * * * * * * * * '''