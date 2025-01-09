n=int(input("n: "))
for i in range(n+1):
    for j in range(2*n+1):
        if i==j or i+j==2*n or i==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

'''* * * * * * * 
     *       *
       *   * 
         *            '''