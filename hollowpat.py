c=int(input("Enter the no of col:"))
r=int(input("Enter the no of rows:"))

def hollow(c,r):
    for i in range(1,c+1):
        for j in range(1,r+1):
            if(i==1 or i==c or j==1 or j==r):
                print("*",end="")
            else:
                print(" ",end="")

        print("")

hollow(c,r)