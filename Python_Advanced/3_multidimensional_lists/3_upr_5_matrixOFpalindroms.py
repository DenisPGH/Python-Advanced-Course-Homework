row, col=[int(x) for x in input().split()]
matrix=[]
start_ascii=97
for r in range(row):
    matrix.append([])
    for c in range(col):
        matrix[r].append("a")

for rr in range(row):
    for cc in range(col):
        matrix[rr][cc]=f"{chr(start_ascii+rr)}{chr(start_ascii+rr+cc)}{chr(start_ascii+rr)}"





for a in range(row):
    print(' '.join(matrix[a]))