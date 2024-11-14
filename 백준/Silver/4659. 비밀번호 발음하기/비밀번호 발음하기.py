vowels = ['a','e','i','o','u']
while True:
    word = input()
    if word == 'end':
        break
    vowel,vowel_cont = 0,0
    conso_cont = 0
    flag = True
    if word[0] in vowels:
        vowel += 1
        vowel_cont += 1
    else:
        conso_cont += 1
    for i in range(1,len(word)):
        if word[i] in vowels:
            if conso_cont:
                conso_cont = 0
            vowel_cont += 1
            vowel += 1
        else:
            if vowel_cont:
                vowel_cont = 0
            conso_cont += 1
        if vowel_cont == 3 or conso_cont == 3:
            flag = False
            break
        if word[i] == word[i-1] and word[i] not in ['e','o']:
            flag = False
            break
    if vowel < 1:
        flag = False
    if flag:
        print(f'<{word}> is acceptable.')
    else:
        print(f'<{word}> is not acceptable.')