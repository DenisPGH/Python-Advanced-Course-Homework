# 4 5
# 1 5 5 2 4
# 2 1 4 14 3
# 3 7 11 2 8
# 4 8 12 16 4

row, col=[int(x) for x in input().split()]
matrix=[]
for r in range(row):
    matrix.append([int(x) for x in input().split()])

#print(matrix)
max_num= -9999999999999999999999999
max_numbers=[]
for r in range(row-2):
    for c in range(col-2):
        group_num=[matrix[r][c],matrix[r][c+1],matrix[r][c+2],
                   matrix[r+1][c],matrix[r+1][c+1],matrix[r+1][c+2],
                   matrix[r+2][c],matrix[r+2][c+1], matrix[r+2][c+2]]
        if sum(group_num)>max_num:
            max_num=sum(group_num)
            max_numbers=group_num



print(f"Sum = {max_num}")
print(" ".join([str(x) for x in max_numbers[:3]]))
print(" ".join([str(x) for x in max_numbers[3:6]]))
print(" ".join([str(x) for x in max_numbers[6:]]))

