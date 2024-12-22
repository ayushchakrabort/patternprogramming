n=int(input("n: "))
val=1
for i in range(n):  
    for j in range(n):
        if i+j>=n-1:
            if i%2==0:
                print(val,end=" ")
            else:
                print("*",end=" ")
        else:
            print(" ",end=" ")
    if i%2==0:
        val+=1
        if val>9:
            val=1
    print()