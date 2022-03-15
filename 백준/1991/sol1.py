import sys

sys.stdin = open('input.txt')

n = int(input())
tree = {}
for i in range(1, n+1):
    node, left, right = input().split()
    tree[node] = [left, right]

print(tree)
