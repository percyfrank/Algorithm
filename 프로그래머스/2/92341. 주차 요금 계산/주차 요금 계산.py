import math

def solution(fees, records):

    car = {}
    for record in records:
        time, num, inout = record.split(" ")
        h,s = map(int,time.split(":"))
        time = h * 60 + s
        if inout == "IN":
            car.setdefault(num,0)
            car[num] -= time
        elif inout == "OUT":
            car[num] += time
    
    
    car = dict(sorted(car.items(),key=lambda x:x[0]))  
    l_time = 23 * 60 + 59
    answer = []
    for num, total in car.items():
        if total <= 0:
            car[num] += l_time
            
        if car[num] <= fees[0]:
            answer.append(fees[1])
        else:
            remain = math.ceil((car[num] - fees[0]) / fees[2])
            answer.append(fees[1]+ remain*fees[3])
    
    return answer