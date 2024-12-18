side=int(input("Enter the number of side: "))
val=1
for i in range(side):
    for j in range(side):
        if j%2==0:
            print("*",end=" ")
        else:
            print(val,end=" ")
            val+=1
            if val>9:
                val=1
    print()

''' * 1 * 2 * 
    * 3 * 4 *
    * 5 * 6 *
    * 7 * 8 *
    * 9 * 1 *'''