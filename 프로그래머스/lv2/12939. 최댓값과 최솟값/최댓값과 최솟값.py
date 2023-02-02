def solution(s):
    answer = ''
    str_list = s.split()
    num_list = []
    for i in str_list:
        num = int(i)
        num_list.append(num)
    max_num = max(num_list)
    min_num = min(num_list)
    answer = str(min_num) + " " + str(max_num)
    return answer