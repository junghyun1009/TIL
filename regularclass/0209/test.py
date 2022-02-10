n = 10
box_height = [93,86,3,81,14,28,3,100,28,26,44,25,24,73,62,82,4,33]

cnt = 0

while True:

    if cnt == n:
        break
    
    max_height = box_height[0]
    min_height = box_height[0]
    max_idx = 0
    min_idx = 0

    for box in range(len(box_height)):
        
        if box_height[box] >= max_height:
            max_height = box_height[box]
            max_idx = box

    box_height[max_idx] -= 1
    
    for box in range(len(box_height)):

        if box_height[box] <= min_height:
            min_height = box_height[box]
            min_idx = box

    box_height[min_idx] += 1
    
    cnt += 1

max_height = box_height[0]
min_height = box_height[0]

for box in range(len(box_height)):
    if box_height[box] >= max_height:
        max_height = box_height[box]

    if box_height[box] <= min_height:
        min_height = box_height[box]

# box_final = box_height[:]
# max_final = box_final[0]
# min_final = box_final[0]

# for box in range(len(box_final)):
#     if box_final[box] >= max_final:
#         max_final = box_final[box]

#     if box_final[box] <= min_final:
#         min_final = box_final[box]

print(f'{(max_height-min_height)}')