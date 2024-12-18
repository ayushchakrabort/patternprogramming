side=int(input("Enter the number of side: "))
for i in range(side):
    for j in range(side):
        if i%2==0:
            print("*",end=" ")
        else:
            print("#",end=" ")
    print()

''' * * * * 
    # # # #
    * * * *
    # # # #'''