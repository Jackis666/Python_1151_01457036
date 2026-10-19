def ck(s):
    try:
        n=float(s)
    except ValueError:
        raise ValueError("Error: please enter a number")
    if '.' in s:
        raise ValueError("Error: please enter an integer")
    n=int(s)
    if n<0 or n>50:
        raise ValueError("Error: number out of range")
    return n
    
s=input().strip()
ok=True
try:
    n=ck(s)
except ValueError as e:
    print(e)
    # print("You guessed 0 times.")
    ok=False
cnt=0
if ok:
    while True:
        s=input().strip()
        okk=0
        try:
            nn=ck(s)
            if nn==n:
                print("You got it!")
                okk=1

            elif nn<n:
                print("You are too low!")
            else:
                print("You are too high!")
        except ValueError as e:
            print(e)
        finally:
            cnt=cnt+1
        if okk:
            break
        
print(f"You guessed {cnt} times.")