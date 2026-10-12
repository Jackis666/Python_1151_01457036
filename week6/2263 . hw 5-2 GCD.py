def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
while True:
    n=int(input())
    if n==0:
        break
    ans=0
    for i in range(1,n):
        for j in range(i+1,n+1):
            ans+=gcd(i,j)
    print(ans)