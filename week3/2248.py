n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
bb=set(b)
ans=[]
cc=0
for c in a :
    if(c in bb):
        ans.append(c);
        cc+=1;
print(cc)
ans.sort()
print(*ans)