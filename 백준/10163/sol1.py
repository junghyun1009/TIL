import sys

sys.stdin = open('input.txt')

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]


