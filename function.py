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

    def shape(self,n):
        for i in range(n):
            for j in range(n):
                if i >=j:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    def shape2(self,n):
        for i in range(n):
            for j in range(n):
                if i <=j:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    def shape3(self,n):
        for i in range(n):
            for j in range(n):
                if i==j:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()            
    def shape4(self,n):
        for i in range(n):
            for j in range(n):
                if i+j>=n-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    def shape5(self,n):
        for i in range(n):
            for j in range(n):
                if i+j<=n-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    def shape6(self,n):
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

    def shape7(self,n):
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

    def shape8(self,n):
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

    def shape9(self,n):
        n=int(input ("n: "))
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i==j or i+j==n+1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    def shape10():
        n=int(input("n: "))
        for i in range(n):
            for j in range(n):
                if i==n-1 or j==n-1 or i==0 or j==0:
                    print("*",end=" ")
                else:    
                    print(" ",end=" ")
            print()

    def shape11(self,n):
        n=int(input("n: "))
        for i in range(n):
            for j in range(n):
                if i==n-1 or j==n-1 or i==0 or j==0 or (i==n//2 and j==n//2):
                    print("*",end=" ")
                else:    
                    print(" ",end=" ")
            print()

    def shape12():
        n=int(input("n: "))
        for i in range(n):
            for j in range(n):
                if i==0 or j==0 or i==n-2 or j==n-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    def shape13(self,n):
        n=int(input("n: "))
        for i in range(n):
            for j in range(n):
                if i==j or i==n-1 or j==0:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
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
# obj.ptrn9(5)
# obj.shape(5)
# obj.shape2(5)
# obj.shape3(5)
# obj.shape4(5)
# obj.shape5(5)
# obj.shape6(5)
# obj.shape7(5)
# obj.shape8(5)
# obj.shape9(5)
# obj.shape10(5)
# obj.shape11(5)
# obj.shape12(5)
obj.shape13(5)


