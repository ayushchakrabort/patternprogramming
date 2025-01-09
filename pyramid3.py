n=int(input("n: "))
for i in range(n+1):
    for j in range(2*n-1):
        if i+j==n-1 or j-i==n-1 or (i == n - 1 and j % 2 == 0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

'''     *
      *   *
    *       *
  *           *
*   *   *   *   *   '''