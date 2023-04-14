def solution(citations):
    answer = 0
    citations.sort()
    # print(citations)
    
    for i in range(citations[len(citations)-1]+1):
        cnt = 0
        for j in citations:
            if  j >= i:
                cnt += 1
        if cnt >= i:
            answer = i
    
    return answer