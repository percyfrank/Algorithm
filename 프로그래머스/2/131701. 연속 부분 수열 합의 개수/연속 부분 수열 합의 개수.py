def solution(elements):
    
    length = len(elements)
    elements = elements * 2
    
    tmp = set()
    for i in range(1,length+1):
        for j in range(length):
            tmp.add(sum(elements[j:j+i]))
    
    return len(tmp)