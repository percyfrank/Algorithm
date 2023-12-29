def solution(arr):
    
#     a,b = arr[0],arr[1]
#     while b > 0:
#         a,b = b,a%b
    
#     answer = a
#     for num in arr:
#         answer *= num // a
    
    lcs = sorted(arr)[-1]
    while True:
        cnt = 0
        for num in arr:
            if lcs % num != 0:
                lcs += 1
                break
            else:
                cnt += 1
        if cnt == len(arr):
            return lcs
    
    # return answer