def ck(s):
    if len(s)!=2:
        raise ValueError("Error: invalid data format")
    if s[1].strip() == "":
            raise ValueError("Error: invalid data format")
    try:
        n=int(s[1])
    except ValueError:
        raise ValueError("Error: invalid score")
    if n<0 or n>100:
        raise ValueError("Error: invalid score")
    return n
_=int(input())
cnt=0
cc=0
for __ in range(_):
    a=input().split(',')
    try:
        n=ck(a)
    except ValueError as e:
        print(e)
    else:
        cnt=cnt+n
        cc+=1
        print("OK")
if cc>0:
    print(f"Average score: {cnt/cc:.2f}")
else:
    print("No valid scores")
