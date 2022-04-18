# 2
# 1, 2, 3
# 4, 5, 6
num_rows=int(input())
matrix=[]
for r in range(num_rows):
    matrix.extend([int(x) for x in input().split(", ")])

print(matrix)
