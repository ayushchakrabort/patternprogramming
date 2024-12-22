n=int(input("n: "))
val=1
p=True
for i in range(1,n+1):  
    for j in range(1,n+1):
        if p==True:
            print(val,end=" ")
            val+=1
            if val>9:
                val=1
            p=False
        else:
            print("*",end=" ")
            p=True
    print()

''' 1 * 2 * 3 
    * 4 * 5 *
    6 * 7 * 8
    * 9 * 1 *
    2 * 3 * 4'''