n,k=map(int,input().split())
a=list(map(int,input().split()))
ans=0
l=0
now=0
for r in range(n):
    now+=a[r]
    while now>k and l<=r:
        now-=a[l]
        l=l+1
    ans=max(ans,r-l+1)
print(ans)