import os
#n=int(input())
a=[]
inn=int(input())
a.append(inn)
print(a[0])
cnt=1
#n-=1
while True: 
    try:
        inn=int(input())
    except EOFError:
        break

    ok=False
    for j in range(cnt):
        if(a[j]>inn):
            a.insert(j,inn)
            ok=True
            break
    if not ok:
        a.append(inn)
    cnt+=1
    if(cnt&1):
        print(a[cnt//2])
    else:
        print((a[cnt//2]+a[cnt//2-1])//2)
    #n-=1
    

