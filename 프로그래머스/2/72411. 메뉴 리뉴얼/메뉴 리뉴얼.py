from itertools import combinations
 
def solution(orders, course):
    
    answer = []
    for c in course:
        tmp = {}
        for order in orders:
            if len(order) < c:
                continue
            for data in combinations(sorted(order),c):
                tmp.setdefault(''.join(data),0)
                tmp[''.join(data)] += 1

        if tmp:
            for key, value in tmp.items():
                if value == max(tmp.values()) >= 2:
                    answer.append(key)
        
    return sorted(answer)