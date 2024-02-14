def solution(storey):

    answer = 0
    while storey > 0:
        storey,r = divmod(storey,10)
        if r > 5 or (r == 5 and storey % 10 >= 5):
            answer += 10 - r
            storey += 1
        else:
            answer += r
            
    return answer