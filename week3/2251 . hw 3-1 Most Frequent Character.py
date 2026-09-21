t=int(input())
for _ in range(t):
    s=str(input())
    b={}
    for c in s:
        b[c]=b.get(c,0)+1
    mx=0
    ans='c'
    for u,v in b.items():
        if(v>mx):
            mx=v
            ans=u
    print(ans)
