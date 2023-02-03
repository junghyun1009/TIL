def solution(brown, yellow):
    answer = []
    area = brown + yellow
    length = brown + 4
    
    for i in range(1, area + 1):
        if area % i == 0:
            width = area // i
            height = i
            if width + height == length // 2:
                answer = [width, height]
                answer.sort(reverse = True)
                break
    return answer