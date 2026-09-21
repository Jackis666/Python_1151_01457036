n=int(input())
while(True):
    a=list(map(int,input().split()))
    if a[0]==0:
        break;
    st=[0]*n
    b=[i for i in range(1,n+1)]
    i=0
    j=-1
    k=0
    while i<n:
        st[j+1]=b[i]
        j+=1
        i+=1
        while(j>-1):
            if st[j]==a[k]:
                j-=1
                k+=1
            else:
                break
    if j==-1:
        print("YES")
    else:
        print("NO")
                

