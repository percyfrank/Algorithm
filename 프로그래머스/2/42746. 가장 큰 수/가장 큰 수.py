def solution(numbers):
    
    nums = []
    for i,num in enumerate(numbers):
        strNum = str(num)*3
        nums.append((i,strNum))

    nums.sort(key=lambda x:x[1],reverse=True)
    answer = ''
    for idx,num in nums:
        answer += str(numbers[idx])
    
    return answer if answer[0] != '0' else '0'