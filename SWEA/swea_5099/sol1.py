import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    
    n, m = map(int, input().split())    # n:화덕의 크기, m:피자 개수
    a = list(map(int, input().split()))     # 각 피자의 치즈에 대한 정보
    pizza = []      # 피자의 번호와 치즈를 함께 저장할 리스트

    for i in range(m):      # 피자의 번호와 치즈를 함께 리스트로 묶어 저장
        pizza.append([i+1, a[i]])

    queue = []      # 화덕
    # print(pizza)

    for j in range(n):      # 화덕의 크기만큼만 큐에 넣어줌
        queue.append(pizza[j])

    for _ in range(n):      # 남아있는 피자에서 제거
        pizza.pop(0)

    # print(queue)
    # print(pizza)

    while True:
        if len(queue) == 1:     # 화덕에 피자가 한개 남아있으면 마지막 피자이므로 중단
            last = queue[0][0]      # 마지막 피자의 번호 저장하고 중단
            break

        out = queue.pop(0)      # 1번 자리에 온 피자 꺼내보기
        out[1] = out[1] // 2        # 치즈 양 절반으로 줄여주기
        if out[1] == 0:     # 치즈가 안 남았다면
            if pizza:       # 남아있는 피자가 있을 경우
                queue.append(pizza[0])      # 화덕에 피자 넣어주기
                pizza.pop(0)        # 피자 목록에서 제거
            
            else:       # 피자가 더 이상 없다면 피자 넣어주는 작업은 할 수 없음
                continue

        else:       # 치즈가 아직 남아있다면 화덕의 맨 뒷자리로 보내주기
            queue.append(out)
    
    print(f'#{tc} {last}')

