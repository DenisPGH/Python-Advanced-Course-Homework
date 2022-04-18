n=int(input())
matrix=[]
for row in range(n):
    matrix.append(list(input()))
searched_char=input()
# 3
# ABC
# DEF
# X!@
# !
position=()
founded=False
for row in range(n):
    for col in range(n):
        if searched_char== matrix[row][col]:
            position=row,col
            founded=True
            break
    if founded:
        break

if founded:
    print(position)
else:
    print(f"{searched_char} does not occur in the matrix")
