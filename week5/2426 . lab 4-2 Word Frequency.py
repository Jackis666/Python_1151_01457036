s=str(input())
ss=s.lower().split()
mp=dict()
for c in ss:
    mp[c]=mp.get(c,0)+1
a=list(mp)
for c,v in mp.items():
    print(c,end=" ")
    print(v)
