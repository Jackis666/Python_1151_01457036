n,m=map(int,input().split())
a=map(int,input().split())
i=0
b={}
for x in a :
    b[x]=i
    i += 1

while m > 0 :
    m-=1
    cnt=int(input())
    print(b.get(cnt,-1))

    

