class PATTERN:
    def rectangle(self,row,col):
        for i in range(row):
            for j in range(col):
                print("*",end=" ")
            print()

    def square(self,side):
        for i in range(side):
            for j in range(side):
                print("*",end=" ")
            print()

    def ptrn(self,row,col):
        val =1
        for i in range(row):
            for j in range(col):
                print(val,end=" ")
                val+=1
                if val>9:
                    val=1
            print()

    def ptrn1(self,side):
        for i in range(side):
            val=1
            for j in range(side):
                print(val,end=" ")
                val+=1
                if val>9:
                    val=1
            print()

    def ptrn2(self,row,col):  
        val=1
        for i in range(row):    
            for j in range(col):
                print(val,end=" ")
            val+=1
            if val>9:
                val=1
            print()

    def alphaptrn2(self,side):
        for i in range(side):
            for j in range(side):
                print(chr(65+i),end=" ")
            print() 

    def alphabetpattern(self,side):   
        for i in range(side): 
            val=0   
            for j in range(side):
                print(chr(65+val),end=" ")
                val+=1
            print()

    def ptrn3(self,side):
        for i in range(side):
            for j in range(side):
                if i%2==0:
                    print("*",end=" ")
                else:
                    print("#",end=" ")
            print()

    def ptrn4(self,side):
        val = 1
        for i in range(side):
            for j in range(side):
                if i%2==0:
                    print("*",end=" ")
                else:
                    print(val,end=" ")
                    val+=1
                    if val>9:
                        val=1        
            print()

    def ptrn5(self,side):
        val=1
        for i in range(side):
            for j in range(side):
                if j%2==0:
                    print("*",end=" ")
                else:
                    print(val,end=" ")
                    val+=1
                    if val>9:
                        val=1
            print()

    def ptrn6(self,side):
        val=1 
        for i in range(side):
            for j in range(side):
                if j%2==0:
                    print("*",end=" ")
                else:
                    print(val,end=" ")
            val+=1
            if val>9:
                val=1
            print()

    def ptrn7(self,side):
        val=1
        for i in range(side):
            for j in range(side):
                if j%2==0:
                    print(val,end=" ")
                else:
                    print(chr(64+val),end=" ")
            val+=1
            print()

    def ptrn8(self,side):
        val=0
        for i in range(side):
            for j in range(1,side+1):
                if j%2!=0:
                    print(j,end=" ")
                else:
                    print(chr(65+val),end=" ")
                    val+=1
            print()

    def ptrn9(self,side):
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
obj=PATTERN()
# obj.rectangle(4,5)
# obj.square(3)
# obj.ptrn(4,5)
# obj.ptrn1(4)
# obj.ptrn2(4,4)
# obj.alphaptrn2(4)
# obj.alphabetpattern(4)
# obj.ptrn3(4)
# obj.ptrn4(6)
# obj.ptrn5(4)
# obj.ptrn6(5)
# obj.ptrn7(5)
# obj.ptrn8(5)
obj.ptrn9(5)




