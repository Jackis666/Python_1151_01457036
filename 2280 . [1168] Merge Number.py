from functools import *
import os
def cmp(a,b):
    return -1 if a+b>b+a else 1

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(str,input().split()))
    a.sort(key=cmp_to_key(cmp))
    for c in a:
        print(c,end='')
    print("")

    