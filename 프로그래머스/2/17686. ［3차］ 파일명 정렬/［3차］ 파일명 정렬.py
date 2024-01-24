def solution(files):

    answer = []
    for file in files:      
        head = number = tail = ""
        flag = False
        for i in range(len(file)):
            if file[i].isdigit():
                number += file[i]
                flag = True
            elif not flag:
                head += file[i]
            else:
                tail = file[i:]
                break
                
            # if len(number) == 5:
            #     answer.append([head,number,file[i:]])
            #     break
        
        answer.append([head,number,tail])
    
    answer.sort(key=lambda x :(x[0].lower(),int(x[1])))
    
    return [''.join(i) for i in answer]

