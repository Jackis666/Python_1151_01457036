def qs(arr):
    if len(arr)<=1:
        return arr
    prv=arr[-1]
    cc=arr[:-1]
    ls=[x for x in cc if x<prv]
    mr=[x for x in cc if x>=prv]
    return qs(ls)+[prv]+qs(mr)




a=list(map(int,input().split()))
print(*qs(a))
