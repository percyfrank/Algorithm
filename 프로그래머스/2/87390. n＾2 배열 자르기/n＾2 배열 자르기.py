def solution(n, left, right):
    
    answer = []
    for num in range(left,right+1):
        row = num // n
        col = num % n
        answer.append(max(row,col)+1)
    
    return answer