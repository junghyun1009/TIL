import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):

    a = input()                                 # 찾고 싶은 문자열
    b = input()                                 # 전체 문자열
    flag = 0                                    # 찾고 싶은 문자열과 일치하는지 확인하는 용도

    for idx in range(len(b)-(len(a)-1)):        # 처음부터 마지막까지 len(a)크기로 한칸씩 옮겨가며 slicing
        tmp = b[idx:idx+len(a)]
        if tmp == a:                            # tmp와 a가 같다면 flag를 1로 바꾸고 중단
            flag = 1
            break

    print(f'#{tc} {flag}')


    # find = 0
    # flag = 0
    # cnt = 0
    #
    # while True:
    #
    #     if find == len(a) or (cnt == len(b) and flag == 0):
    #         break
    #
    #     for idx in range(len(b)):
    #         if b[idx] == a[find]:
    #             flag = 1
    #             find += 1
    #             cnt += 1
    #             if find == len(a):
    #                 break
    #             else:
    #                 continue
    #
    #         else:
    #             if flag == 1:
    #                 flag = 0
    #                 find = 0
    #                 cnt += 1
    #
    #             else:
    #                 flag = 0
    #                 cnt += 1
    #
    #
    #

