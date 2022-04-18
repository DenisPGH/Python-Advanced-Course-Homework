# 3
# 11 2 4
# 4 5 6
# 10 8 -12
num_row=int(input())
matrix=[]
for r in range(num_row):
    matrix.append([int(x) for x in input().split()])
result=0
for ccc in range(num_row):
    result+=matrix[ccc][ccc]
print(result)