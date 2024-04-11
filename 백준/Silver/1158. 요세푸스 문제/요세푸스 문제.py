n,k = map(int,input().split())
q = [i for i in range(1,n+1)]
arr = []
idx = 0

while q:
    idx += k-1
    if idx >= len(q):
        idx %= len(q)
    arr.append(str(q.pop(idx)))

print("<" + ", ".join(arr) + ">")