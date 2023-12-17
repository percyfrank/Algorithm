def solution(n):
    answer = 0
    
    cnt = bin(n)[2:].count("1")
    
    while True:
        n += 1
        tmp = bin(n)[2:]
        if cnt == tmp.count("1"):
            return n
