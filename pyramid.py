n=int(input("n: "))
val1=n-1
val2=1
for i in range(n):
    for j in range(val1):
        print(" ",end=" ")
    for k in range(val2):
        print("*",end=" ")
    val2+=2
    val1-=1    
    print()

