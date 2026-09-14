n=int(input())
if n<=1:
    print("Invalid input")
else:
    for i in range(2*n-1):
        for j in range(2*n-1):
            if(abs(j-n+1)==n-1-abs(i-n+1)):
                print("*",end="")
            else:
                print(" ",end="")
        print("")