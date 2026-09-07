import sys

input = sys.stdin.readline

n,m,k=map(int,input().split())

a=[]
for _ in range(n):
    cnt=list(map(int,input().split()))
    a.append(cnt)
b={}
for i,_ in enumerate(a):
    for j,c in enumerate(_) :
        b[c]=(i,j)
while k>0 :
    k-=1
    cnt=int(input())
    if cnt in b:
        print(*b[cnt])
    else :
        print(-1)