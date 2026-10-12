def ff(*arg):
    ans=0
    for c in arg:
        if c%2==0:
            ans+=c
    print(ans)
while True:
    a=input().strip()
    if a=="END":
        break
    else :
        b=list(map(int,a.split()))
        ff(*b)