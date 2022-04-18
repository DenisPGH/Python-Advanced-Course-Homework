# 3
# 1, 2, 3
# 4, 5, 6
# 7, 8, 9
numb=int(input())
matrix= [[int(x) for x in input().split(", ")] for _ in range(numb)]
#print(matrix)
prim_diagonal=[]
prim_sum=0
second_sum=0
second_diagonal=[]
for n in range(numb):
    prim_diagonal.append(matrix[n][n])
    second_diagonal.append(matrix[n][(numb-1)-n])

prim_sum=sum(prim_diagonal)
second_sum=sum(second_diagonal)



print(f"Primary diagonal: {', '.join([str(x) for x in prim_diagonal])}. Sum: {prim_sum}")
print(f"Secondary diagonal: {', '.join([str(x) for x in second_diagonal])}. Sum: {second_sum}")
