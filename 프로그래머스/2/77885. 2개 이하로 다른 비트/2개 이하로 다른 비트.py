def solution(numbers):
    
    answer = []
    for num in numbers:
        number = '0' + bin(num)[2:]
        idx = number.rfind('0')
        number = list(number)
        number[idx] = '1'
        
        if num % 2 == 1:
            number[idx+1] = '0'
        
        answer.append(int(''.join(number),2))
        
    return answer
