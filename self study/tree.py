# 전위 순회
def preorder(node):
    print(node, end='')
    left, right = tree[node][0], tree[node][1]
    # 가장 자손이 아니면
    if left != '.':
        preorder(left)
    if right != '.':
        preorder(right)

# 중위 순회
def inorder(node):
    left, right = tree[node][0], tree[node][1]
    if left != '.':
        inorder(left)
    print(node, end='')
    if right != '.':
        inorder(right)

# 후위 순회
def postorder(node):
    left, right = tree[node][0], tree[node][1]
    if left != '.':
        postorder(left)
    if right != '.':
        postorder(right)
    print(node, end='')

N = int(input())
tree = {}
for i in range(1, N + 1):
    node, left, right = input().split()
    tree[node] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')
