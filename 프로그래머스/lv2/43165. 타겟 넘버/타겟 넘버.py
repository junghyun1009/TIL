def solution(numbers, target):
    answer = 0
    sign = []
    def dfs(arr):
        if len(arr) == len(numbers):
            sign.append(arr)
            return
        for i in ['-', '+']:
            dfs(arr+[i])
    dfs([])
    for s in sign:
        cal = 0
        for idx in range(len(numbers)):
            if s[idx] == '-':
                cal -= numbers[idx]
            else:
                cal += numbers[idx]
        if cal == target:
            answer += 1
    return answer