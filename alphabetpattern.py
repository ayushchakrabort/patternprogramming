side=int(input("Enter the number of side: "))
for i in range(side): 
    val=0   
    for j in range(side):
        print(chr(65+val),end=" ")
        val+=1
    print()

    ''' A B C D 
        A B C D
        A B C D
        A B C D'''