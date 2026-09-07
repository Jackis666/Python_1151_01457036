from functools import *
import os

t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    aa=list(map(int,input().split()))
    b={}
    for i,c in enumerate(aa):
        b[c]=i;
    a.sort(key=lambda x:(b.get(x,1000000),x))
    print(*a)

    