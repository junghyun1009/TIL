
while True:
    password = input()
    
    if password == 'end':
        break

    flag = 0
    vowel = ['a', 'e', 'i', 'o', 'u']

    # 1. 모음 하나 반드시 포함
    cnt_vowel = 0
    for p in password:
        if p in vowel:
            cnt_vowel += 1
    if cnt_vowel == 0:
        flag = 1

    # 2. 모음 3개 혹은 자음 3개 연속 안됨
    check = []
    for i in password:
        if i in vowel:
            check.append(0)
        else:
            check.append(1)

    for c in range(len(check)):
        if check[c:c+3] == [0, 0, 0] or check[c:c+3] == [1, 1, 1]:
            flag = 1
            break

            
    # 3. 같은 글자 연속 두번 안됨
    if len(password) >= 2:
        for j in range(len(password)-1):
            tmp = password[j:j+2]
            if (tmp[0] == tmp[1]) and (tmp != 'ee') and (tmp != 'oo'):
                flag = 1
                break

    if flag == 1:
        print('<' + password + '>' + ' is not acceptable.')
    else:
        print('<' + password + '>' + ' is acceptable.')
