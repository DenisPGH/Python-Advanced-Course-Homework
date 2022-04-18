# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0
summ=0
matrix=[]
row,col= [int(x) for x in input().split(", ")]
for r in range(row):
    numbers= [int(x) for x in input().split(", ")]
    matrix.append(numbers)
    summ+=sum(numbers)

print(summ)
print(matrix)

