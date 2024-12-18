side=int(input("Enter the number of side: "))
val=0
for i in range(side):
    for j in range(1,side+1):
        if j%2!=0:
            print(j,end=" ")
        else:
            print(chr(65+val),end=" ")
            val+=1
    print()


''' 1 A 3 B 5 
    1 C 3 D 5
    1 E 3 F 5
    1 G 3 H 5
    1 I 3 J 5'''