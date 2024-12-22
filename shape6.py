n=int(input("n: "))
val1=1
val2=1
for i in range(n):  
    for j in range(n):
        if i==j:
            print("*",end=" ")
        elif i>j:
            print(val1,end=" ")
            val1+=1
            if val1>9:
                val1=1
        else:
            print(val2,end=" ")
            val2+=1
            if val2>9:
                val2=1
    print()


''' * 1 2 3 4 
    1 * 5 6 7
    2 3 * 8 9
    4 5 6 * 1
    7 8 9 1 *'''