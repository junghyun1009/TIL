import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))

    queue = []      # 큐에 주어진 숫자들을 차례로 넣어준다
    for i in numbers:
        queue.append(i)

    for j in range(m):      # 주어진 횟수만큼 맨 앞에서 빼서 다시 맨 뒤에 넣어준다
        a = queue.pop(0)
        queue.append(a)
    
    print(f'#{tc} {queue[0]}')      # 큐의 가장 앞 원소 출력

