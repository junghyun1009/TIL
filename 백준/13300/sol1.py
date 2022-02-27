import sys

sys.stdin = open('input.txt')

# n = 총 학생 수, k = 한 방 최대 인원 수
n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# 여자, 남자, 학년
students = [[0, 0, 1], [0, 0, 2], [0, 0, 3], [0, 0, 4], [0, 0, 5], [0, 0, 6]]

for i in a:
    for j in students:
        if i[1] == j[2]:
            j[i[0]] += 1

room = 0
for i in students:
    for j in range(2):
        if i[j] % k != 0:
            room += i[j] // k + 1
        else:
            room += i[j] // k

print(room)