n=int(input())
if n<=0:
    print("Invalid input")
else:
    cnt=1
    for i in range(n+1):
        for j in range(i): 
            print(cnt,end=" ")
            cnt+=1
        print("")
