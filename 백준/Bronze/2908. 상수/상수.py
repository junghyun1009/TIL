A, B = input().split()

new_A = int(A[::-1])
new_B = int(B[::-1])

print(max(new_A, new_B))