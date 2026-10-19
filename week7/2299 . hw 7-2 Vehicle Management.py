class vehicle:
    def __init__(self,name,year):
        self.name=name
        self.year=year
    def printf(self):...
class car(vehicle):
    def __init__(self, name, year,n):
        super().__init__(name, year)
        self.seat=n
    def printf(self):
        print(f"Car: {self.name}, Year: {self.year}, Seat: {self.seat}")
class motorcycle(vehicle):
    def __init__(self, name, year,n):
        super().__init__(name, year)
        self.cc=n
    def printf(self):
        print(f"Motorcycle: {self.name}, Year: {self.year}, cc: {self.cc}")
class bicycle(vehicle):
    def __init__(self, name, year,n):
        super().__init__(name, year)
        self.model=n
    def printf(self):
        print(f"Bicycle: {self.name}, Year: {self.year}, Model: {self.model}")

now=list([])
while 1:
    a=input().strip().split()
    if not a:
        continue
    if(a[0]=="stop"):
        break
    if(a[0]=="print"):
        for i in now:
            i.printf()
    if(a[0]=="Car"):
        now.append(car(a[1],a[2],a[3]))
    if(a[0]=="Motorcycle"):
        now.append(motorcycle(a[1],a[2],a[3]))
    if(a[0]=="Bicycle"):
        now.append(bicycle(a[1],a[2],a[3]))

