N = int(input())
score = list(map(int, input().split()))

max_score = max(score)

new_score = []
for i in score:
    new_score.append(i / max_score * 100)

ans = sum(new_score) / N

print(ans)
