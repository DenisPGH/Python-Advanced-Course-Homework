# 5
# 1 3 7 9 11
# X 5 4 X 63
# 7 3 21 95 1
# B 1 73 4 9
# 9 2 33 2 0
import sys


def up(row:int, col:int):
    return row-1, col
def down(row:int, col:int):
    return row+1, col
def left(row:int, col:int):
    return row, col-1
def right(row:int, col:int):
    return row, col+1

size=int(input())
matrix=[]
bunny_row=0
bunny_col=0
# collect the matrix
for r in range(size):
    line=input().split()
    matrix.append(line)
    # finding where is bunny
    for char in range(len(line)):
        if line[char]=="B": # position of the bunny
            bunny_row=r
            bunny_col=char

# finding the must value of eggs
directions={
    "up":  up,
    "down": down,
    "right": right,
    "left": left
}
most_eggs=-sys.maxsize
best_direction=""
best_way=[]
for dir,funk in directions.items():
    cur_eggs=0
    cur_row,cur_col=bunny_row,bunny_col
    cur_way=[]
    while True:
        cur_row,cur_col=funk(cur_row,cur_col)
        if (0 <= cur_row < size and 0 <= cur_col < size) and (matrix[cur_row][cur_col] != "X"):
            cur_eggs+=int(matrix[cur_row][cur_col])
            cur_way.append([cur_row, cur_col])
        else:
            break
    #print(cur_eggs)
    if cur_eggs>most_eggs:
        most_eggs=cur_eggs
        best_direction=dir
        best_way=cur_way

if most_eggs:
    print(best_direction)

    for a in best_way:
        print(a)
if most_eggs:
    print(most_eggs)

# print the matrix
# for rr in range(size):
#     print(*matrix[rr], sep=" ")
#
# print(bunny_row)
# print(bunny_col)
