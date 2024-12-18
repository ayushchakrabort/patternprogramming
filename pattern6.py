side=int(input("Enter the number of side: "))
val=1
for i in range(side):
    for j in range(side):
        if j%2==0:
            print(val,end=" ")
        else:
            print(chr(64+val),end=" ")
    val+=1
    print()

''' 1 A 1 A 1 
    2 B 2 B 2
    3 C 3 C 3
    4 D 4 D 4
    5 E 5 E 5'''