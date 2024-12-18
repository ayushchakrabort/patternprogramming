side=int(input("Enter the number of side: "))
for i in range(side):
    val=1
    for j in range(side):
        print(val,end=" ")
        val+=1
        if val>9:
            val=1
    print()

''' 1 2 3 4 
    1 2 3 4 
    1 2 3 4
    1 2 3 4'''    