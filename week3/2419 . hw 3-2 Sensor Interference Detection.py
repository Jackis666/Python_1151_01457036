n,d=map(int,input().split())
a=[]
for _ in range(n):
    b=list(map(int,input().split()))
    a.append(tuple(b))
a.sort()
ans=[]
sz=0
for i in range(n):
    for j in range(i+1,n):
        dis=(a[i][0]-a[j][0])**2
        dis+=(a[i][1]-a[j][1])**2
        dis+=(a[i][2]-a[j][2])**2
        if dis<=d and a[i][3]!=a[j][3]:
            ans.append((a[i],a[j]))
            sz+=1
print("Interference Pairs: ",end="")
print(sz)
for c in ans:
    print(c[0],end="")
    print(" <-> ",end="")
    print(c[1])
    

