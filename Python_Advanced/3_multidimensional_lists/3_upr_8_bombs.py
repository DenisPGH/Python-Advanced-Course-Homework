def valid_index(x:int,y:int):
    if 0<=x<num and 0<=y< num and (matrix[x][y]>0):
        return True

from collections import deque
# 4
# 8 3 2 5
# 6 4 7 9
# 9 9 3 6
# 6 8 1 2
# 1,2 2,1 2,0
num=int(input())
matrix=[]
for row in range(num):
    matrix.append([int(x) for x in input().split()])
# bomb coordinates
bombs=deque([list([int(x) for x in y.split(',')]) for y in input().split()])


while bombs:
    cur_bomb=bombs.popleft() # remove first bomb from the list
    row=cur_bomb[0]
    col=cur_bomb[1]
    value_bomb=matrix[row][col]
    ###
    if value_bomb>0: # the bomb must be more than zero
        # for r in range(num):
        #     for c in range(num):
        #         if r==cur_bomb[0] and c==cur_bomb[1]: # activate bomb
        if valid_index(row,col+1):
            matrix[row][col+1]-=value_bomb
        if valid_index(row, col - 1):
            matrix[row][col - 1] -= value_bomb
        if valid_index(row-1, col):
            matrix[row-1][col] -= value_bomb
        if valid_index(row+1, col):
            matrix[row+1][col] -= value_bomb

        if valid_index(row-1, col-1):
            matrix[row-1][col-1] -= value_bomb
        if valid_index(row-1, col+1):
            matrix[row-1][col+1] -= value_bomb
        if valid_index(row+1, col-1):
            matrix[row+1][col-1] -= value_bomb
        if valid_index(row+1, col+1):
            matrix[row+1][col+1] -= value_bomb

        matrix[row][col]=0 # bomb equal null

count_alive=0
sum_alive=0
for r in range(num):
    for c in range(num):
        if matrix[r][c]>0:
            count_alive+=1
            sum_alive+= matrix[r][c]


print(f"Alive cells: {count_alive}")
print(f"Sum: {sum_alive}")
for a in range(num):
    print(' '.join([str(x) for x in matrix[a]]))
#print(bombs)





