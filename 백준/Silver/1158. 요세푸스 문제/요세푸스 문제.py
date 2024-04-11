from collections import deque

n,k = map(int,input().split())
q = deque([i for i in range(1,n+1)])

arr = []
while q:
    for _ in range(k-1):
        q.append(q.popleft())
    arr.append(q.popleft())

print(str(arr).replace("[", "<").replace("]", ">"))
