# 2
# 1, 2, 3
# 4, 5, 6
rows=int(input())
matrix=[]
for r in range(rows):
    even_numbers= [int(x) for x in input().split(", ") if int(x)%2==0 ]
    matrix.append(even_numbers)

print(matrix)
