row=int(input("Enter the number of rows: "))
col=int(input("Enter the number of columns: "))
val=1
for i in range(row):    
    for j in range(col):
        print(val,end=" ")
    val+=1
    print()


'''1 1 1 1 
    2 2 2 2
    3 3 3 3'''