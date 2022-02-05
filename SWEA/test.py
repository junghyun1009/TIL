
a = [[1,1,0,1,0,1,1,1],
[0,1,0,1,0,0,0,1],
[1,1,1,0,0,1,0,1],
[0,1,0,1,0,1,1,1],
[0,0,0,1,0,1,0,1],
[1,1,1,1,1,1,0,0],
[0,1,0,0,0,1,0,1],
[1,1,1,0,1,1,1,1]]
# a = [[0,0,1,1,1],[1,1,1,1,0],[0,0,1,0,0],[0,1,1,1,1],[1,1,1,0,1]]
count = 0
b = []

# 가로
tmp_main = []
tmp_a = []

for row in a:
    tmp = []
    # 3개씩 자르면서 합이 3이면 좌우가 0이어야 돼
    # 3개씩 잘라서 3인거니까 나중에 글자수로 바꿔
    for i in range(len(row)-(3-1)):
        tmp.append(row[i:i+3])
        print(sum(tmp))
    #tmp_a.append(sum(tmp))
#print(tmp_a)

    # tmp_sum = []
    # for j in tmp:
    #     tmp_sum.append(sum(j))
    # tmp_main.append(tmp_sum)
    # #print(tmp_main)

#     # if tmp_sum.count(3) == 1:
#     #     count += 1
#     for k in tmp_sum:
#         for i,j in enumerate(k):
            
#             if j==3 :
                
#                 if i==0 and k[i+1]!=3:
#                     count=count+1
                    
#                 elif i==len(k)-1 and  k[i-1]!=3:
#                     count=count+1
#                 elif i!=len(k)-1 and k[i-1]!=3 and k[i+1]!=3 :
#                     count=count+1
#                 else:
#                     pass

#             else:
#                 pass
        


# # 세로
# for i in range(len(a[0])):
#     b_ele = []
#     for j in range(len(a)):
#         b_ele.append(a[j][i])
#     b.append(b_ele)
# #print(b)

# for row in b:
#     tmp = []
#     # 3개씩 자르면서 합이 3이면 좌우가 0이어야 돼
#     # 3개씩 잘라서 3인거니까 나중에 글자수로 바꿔
#     for i in range(len(row)-(3-1)):
#         tmp.append(row[i:i+3])
#     #print(tmp)

#     tmp_sum = []
#     for j in tmp:
#         tmp_sum.append(sum(j))
#     #print(tmp_sum)

#     # if tmp_sum.count(3) == 1:
#     #     count += 1
#     for k in tmp_sum:
#         for i,j in enumerate(k):
            
#             if j==3 :
                
#                 if i==0 and k[i+1]!=3:
#                     count=count+1
                    
#                 elif i==len(k)-1 and  k[i-1]!=3:
#                     count=count+1
#                 elif i!=len(k)-1 and k[i-1]!=3 and k[i+1]!=3 :
#                     count=count+1
#                 else:
#                     pass

#             else:
#                 pass
    

# print(count)