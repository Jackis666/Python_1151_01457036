class Bank:
    def __init__(self,name,n:int):
        self.name=name
        self.money=n
    def add(self,n):
        self.money+=n
    def mi(self,n):
        if self.money<n:
            print("Insufficient funds")
            return False
        self.money-=n
        return True
    def ck(self):
        print(self.money)
mp={}
while 1:
    a=input().strip().split()
    if a[0]=="stop":
        break
    if a[0]=="create":
        mp[a[1]]=Bank(a[1],int(a[2]))
    if a[0]=="deposit":
        if a[1] not in mp:
            print("Account not found")
            continue
        mp[a[1]].add(int(a[2]))
    if a[0]=="withdraw":
            if a[1] not in mp:
                print("Account not found")
                continue
            mp[a[1]].mi(int(a[2]))
    if a[0]=="balance":
            if a[1] not in mp:
                print("Account not found")
                continue
            mp[a[1]].ck()
            


