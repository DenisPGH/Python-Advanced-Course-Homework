# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0
row, col=[int(x) for x in input().split(", ")]
matrix=[]
for r in range(row):
    matrix.append([int(x) for x in input().split(", ")])

#print(matrix)
max_num= -9999999999999999999999999
max_numbers=[]
for r in range(row-1):
    for c in range(col-1):
        group_num=[matrix[r][c],matrix[r][c+1],matrix[r+1][c],matrix[r+1][c+1]]
        if sum(group_num)>max_num:
            max_num=sum(group_num)
            max_numbers=group_num


print(" ".join([str(x) for x in max_numbers[:2]]))
print(" ".join([str(x) for x in max_numbers[2:]]))
print(max_num)
