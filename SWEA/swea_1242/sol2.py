import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):

    n, m = map(int, input().split())        # n:배열 세로, m:배열 가로
    a = list({input() for _ in range(n)})
    print(a)
