def ff():
    n=int(input())
    mp=dict()
    for _ in range(n):
        a,b,c=map(str,input().split())
        mp[a]=(b,c)
    for _ in range(int(input())):
        c=input().strip()
        print(*mp.get(c,("Not","found")))
ff()
