import functools
def ff(func):
    mp={}
    @functools.wraps(func)
    def ch(n):
        if(mp.get(n,-1)==-1):
            mp[n]=func(n)
            print(f"Computed fibonacci({n}) = {mp[n]}")
        else:
            print(f"Cache hit for fibonacci({n})")
            #return mp[n]
        return mp[n]
    return ch
@ff
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n=int(input())
ans=fibonacci(n)
print(f"Final Result: {ans}")
