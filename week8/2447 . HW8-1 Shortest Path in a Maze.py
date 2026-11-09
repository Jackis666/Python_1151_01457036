from collections import deque
class Queue:
    def __init__(self):
        self.items = deque()
    def is_empty(self):
        return len(self.items) == 0
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.popleft()
    def front(self):
        if self.is_empty():
            raise IndexError("Front from empty queue")
        return self.items[0]
    def size(self):
        return len(self.items)



n,m=map(int,input().split())
mp=[]
for i in range(n):
    mp.append(input().strip())
q=Queue()
vis=[[0 for x in range(m)]for x in range(n)]
ed=[0,0]
for x in range(n):
    for y in range(m):
        if mp[x][y]=='S':
            vis[x][y]=1
            q.enqueue([x,y])
        if mp[x][y]=='T':
            ed=[x,y]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
while not q.is_empty():
    x,y=q.dequeue()
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if nx<0 or ny<0 or nx>=n or ny>=m:
            continue
        if vis[nx][ny]!=0:
            continue
        if mp[nx][ny]=='#':
            continue
        vis[nx][ny]=vis[x][y]+1
        q.enqueue([nx,ny])
print(vis[ed[0]][ed[1]]-1)