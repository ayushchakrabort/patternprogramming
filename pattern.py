row=int(input("Enter the number of rows: "))
col=int(input("Enter the number of columns: "))
val =1
for i in range(row):
    for j in range(col):
        print(val,end=" ")
        val+=1
        if val>9:
            val=1
    print()


''' 1 2 3 4 5
    6 7 8 9 1
    2 3 4 5 6'''
