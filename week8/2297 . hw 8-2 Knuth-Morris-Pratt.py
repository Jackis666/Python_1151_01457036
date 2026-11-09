import sys
a=sys.stdin.buffer.readline().strip()
b=sys.stdin.buffer.readline().strip()
ss=b+b"@"+a
n=len(ss)
f=[0]*n
for i in range(1,n):
    j=f[i-1]
    while j>0 and ss[j]!=ss[i]:
        j=f[j-1]
    if ss[j]==ss[i]:
        f[i]=j+1
    else:
        f[i]=j
m=len(b)
ans=[]
for i in range(m+1,n):
    if(f[i]==m):
        ans.append(str(i-2*m))
sys.stdout.write(" ".join(ans))

