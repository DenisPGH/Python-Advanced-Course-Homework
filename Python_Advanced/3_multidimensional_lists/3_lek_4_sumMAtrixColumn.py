# 3, 6
# 7 1 3 3 2 1
# 1 3 9 8 5 6
# 4 6 7 9 1 0

row,col=[int(x) for x in input().split(", ")]
matrix=[]
for r in range(row):
    matrix.append([int(x) for x in input().split()])
#print(matrix)
summ=0
for c in range(col):
    summ=0
    for r in range(row):
        summ+=matrix[r][c]
    print(summ)