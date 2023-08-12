
message = input()
key = input()

table = [[0 for _ in range(5)] for _ in range(5)]
key_set = {}

for i in range(len(key)):
    if key[i] not in key_set:
        table[len(key_set)//5][len(key_set)%5] = key[i]
        key_set[key[i]] = len(key_set)

alphas = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
tmp = len(key_set)
for alpha in alphas:
    if alpha not in key_set:
        table[tmp//5][tmp%5] = alpha
        key_set[alpha] = tmp
        tmp += 1

split_message = []
idx = 0
while True:
    if idx == len(message):
        break
    if idx == len(message)-1:
        split_message.append(message[idx]+'X')
        break
    elif message[idx] == message[idx+1]:
        if message[idx] == 'X':
            split_message.append(message[idx]+'Q')
        else:
            split_message.append(message[idx]+'X')
        idx += 1
    elif message[idx] != message[idx+1]:
        split_message.append(message[idx:idx+2])
        idx += 2

result = ''
for word in split_message:
    loc_1 = key_set[word[0]]
    loc_2 = key_set[word[1]]
    if loc_1//5 == loc_2//5:
        word_1 = table[loc_1//5][(loc_1+1)%5]
        word_2 = table[loc_2//5][(loc_2+1)%5]
    elif loc_1%5 == loc_2%5:
        word_1 = table[(loc_1//5+1)%5][loc_1%5]
        word_2 = table[(loc_2//5+1)%5][loc_2%5]
    else:
        word_1 = table[loc_1//5][loc_2%5]
        word_2 = table[loc_2//5][loc_1%5]
    result += word_1 + word_2

print(result)