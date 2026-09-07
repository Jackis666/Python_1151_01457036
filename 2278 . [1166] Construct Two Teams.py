import sys

input = sys.stdin.readline

t=int(input())
for _ in range(t) :

    n=int(input())
    a=list(map(int,input().split()))
    mp={}
    for c in a :
        mp[c]=mp.get(c,0)+1
    ans=0
    mx=0;
    for c in mp :
        mx=max(mx,mp[c])
    print(max(min(mx,len(mp)-1),min(mx-1,len(mp))),end="\n")

