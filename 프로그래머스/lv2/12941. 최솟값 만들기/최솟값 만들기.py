# def dfs(A, v, arr, rlt):
#     if len(arr) == len(A):
#         rlt.append(arr)
#         return
#     for i in range(len(A)):
#         if v[i] == 0:
#             v[i] = 1
#             dfs(A, v, arr + [A[i]], rlt)
#             v[i] = 0
#     return rlt
import itertools

def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse = True)
    for i in range(len(A)):
        answer += A[i] * B[i]
    # answer = 999999999999999999999999999999999999
    # visited_A = [0] * len(A)
    # visited_B = [0] * len(B)
    # order_A = dfs(A, visited_A, [], [])
    # order_B = dfs(B, visited_B, [], [])
#     order_A = list(set(itertools.permutations(A, len(A))))
#     order_B = list(set(itertools.permutations(B, len(B))))
#     print(order_A)
#     print(order_B)
    
#     for i in (order_A):
#         for j in (order_B):
#             tmp_ans = 0
#             for k in range(len(A)):
#                 tmp_ans += i[k] * j[k]
#                 if tmp_ans >= answer:
#                     break
#             if answer > tmp_ans:
#                 answer = tmp_ans

    return answer