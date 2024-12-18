side=int(input("Enter the number of side: "))
for i in range(side):
    val=0
    for j in range(side):
        if i%2==0:
            print(chr(65+val),end=" ")
            val+=1
        else:
            print(val+1,end=" ")
            val+=1
    print()

''' A B C D E 
    1 2 3 4 5
    A B C D E
    1 2 3 4 5
    A B C D E'''