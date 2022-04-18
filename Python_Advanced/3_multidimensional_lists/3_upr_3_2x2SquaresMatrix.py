# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0
row, col=[int(x) for x in input().split()]
matrix=[]
for r in range(row):
    matrix.append([x for x in input().split()])

#print(matrix)

same_char=[]
counter_same=0
for r in range(row-1):
    for c in range(col-1):
        group_num=[matrix[r][c],matrix[r][c+1],matrix[r+1][c],matrix[r+1][c+1]]
        if matrix[r][c]==matrix[r][c+1]==matrix[r+1][c]==matrix[r+1][c+1]:
            counter_same+=1

print(counter_same)




