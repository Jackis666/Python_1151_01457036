def ff(n):
    ans=n
    cnt=n+1
    while cnt>=3:
        ans=ans+cnt//3
        cnt=cnt%3+cnt//3
    print(ans)
while True:
    try:
        n=int(input())
        ff(n)
    except EOFError:
        break