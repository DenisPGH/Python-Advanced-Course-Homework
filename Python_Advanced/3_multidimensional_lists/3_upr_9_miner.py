"""are:
•	* - a regular position on the field
•	e - the end of the route
•	c - coal
•	s - miner
"""
from collections import deque


def directtions(richtung,row,col):
    if richtung=="up":
        return row-1,col
    if richtung=="down":
        return row + 1, col
    if richtung=="left":
        return row , col-1
    if richtung=="right":
        return row, col+1


def print_matrix(mat):
    for each_row in mat:
        print(' '.join(each_row))

def check_if_coord_outside(row,col,dimes):
    if row<0 or row >=dimes or col<0 or col>=dimes:
        return True
    else:
        return False


size_of_field=int(input())
comand_list=deque(input().split())
matrix=[]
actual_row,actual_col=(0,0)
game_over=False
all_coins_value=0
collected_coins=0
for row in range(size_of_field):
    current_row=input().split()
    matrix.append(current_row)
    for col in range(len(current_row)):
        if current_row[col]=="s": # the miner
            actual_row, actual_col=(row, col)
        if current_row[col]=="c": #
            all_coins_value+=1




while comand_list:
    current_comand=comand_list.popleft()
    next_row,next_col=directtions(current_comand,actual_row,actual_col)
    if check_if_coord_outside(next_row,next_col,size_of_field):
        continue
    if matrix[next_row][next_col]=="e":
        actual_row,actual_col=next_row,next_col
        game_over=True
        break

    if matrix[next_row][next_col]=="c":
        matrix[next_row][next_col] = "s"
        matrix[actual_row][actual_col] = "*"
        collected_coins+=1

    if matrix[next_row][next_col]=="*":
        matrix[next_row][next_col] = "s"
        matrix[actual_row][actual_col] = "*"
    actual_row,actual_col=next_row,next_col




#print_matrix(matrix)

if game_over:
    print(f"Game over! ({actual_row}, {actual_col})")

elif not game_over and collected_coins==all_coins_value:
    print(f"You collected all coal! ({actual_row}, {actual_col})")

else:
    print(f"{all_coins_value-collected_coins} pieces of coal left. ({actual_row}, {actual_col})")