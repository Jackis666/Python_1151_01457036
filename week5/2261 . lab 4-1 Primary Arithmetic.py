def sol(a,b):
    c=0;
    ans=0
    while a>0 or b>0:
        cnt=a%10+b%10+c;
        if cnt>=10:
            ans=ans+1
        a=a//10
        b=b//10
        c=cnt
        c=c//10
    return ans

def main():
    while True:
        a,b=map(int,input().split())
        if a==0 and b==0:
            break;
        ans=sol(a,b)
        if ans==0:
            print("No carry operation.")
        elif ans==1:
            print("1 carry operation.")
        else:
            print(ans,end=" ")
            print("carry operations.")
if __name__ == "__main__":
    main()
