from collections import deque


def print_matrix(mat):
    for each_row in mat:
        print(''.join(each_row))


def generate_matirx_by_row_and_col(row,col,mat):
    for r in range(row):
        mat.append(["."]*col)
    return mat


def directtions(richtung,row,col):
    if richtung=="U":
        return row-1,col
    if richtung=="D":
        return row + 1, col
    if richtung=="L":
        return row , col-1
    if richtung=="R":
        return row, col+1

def check_if_coord_outside(row,col,n,m):
    if row<0 or row >=n or col<0 or col>=m:
        return True
    else:
        return False


def bunny_spreading(list_bunnies,mat,n,m):
    # every step bunny spreads one position up, down, left, and right.
    new_list_bunnies=[]
    died=False
    for each_coord in range(len(list_bunnies)):
        bunny_row,bunny_col=list_bunnies[each_coord]
        # up
        if not check_if_coord_outside(bunny_row - 1, bunny_col, n, m):
            if mat[bunny_row - 1][bunny_col] == ".":
                mat[bunny_row - 1][bunny_col] = "B"
                new_list_bunnies.append((bunny_row - 1,bunny_col))
            elif mat[bunny_row - 1][bunny_col] == "B":
                pass
            else:
                mat[bunny_row - 1][bunny_col] = "B"
                died=True

        # down
        if not check_if_coord_outside(bunny_row + 1, bunny_col, n, m):
            if mat[bunny_row + 1][bunny_col] == ".":
                mat[bunny_row + 1][bunny_col] = "B"
                new_list_bunnies.append((bunny_row + 1, bunny_col))
            elif mat[bunny_row + 1][bunny_col] == "B":
                pass
            else:
                mat[bunny_row + 1][bunny_col] = "B"
                died=True


        # left
        if not check_if_coord_outside(bunny_row , bunny_col-1,n,m):
            if mat[bunny_row ][bunny_col-1] == ".":
                 mat[bunny_row ][bunny_col-1] = "B"
                 new_list_bunnies.append((bunny_row, bunny_col-1))
            elif mat[bunny_row ][bunny_col-1] == "B":
                pass
            else:
                mat[bunny_row][bunny_col - 1] = "B"
                died=True


        # right
        if not check_if_coord_outside(bunny_row , bunny_col+ 1,n,m):
            if mat[bunny_row ][bunny_col+1] == ".":
                 mat[bunny_row ][bunny_col+1] = "B"
                 new_list_bunnies.append((bunny_row , bunny_col+1))
            elif mat[bunny_row ][bunny_col+1] == "B":
                pass
            else:
                mat[bunny_row][bunny_col + 1] = "B"
                died=True
    if died==True:
        return "died"
    else:
        return new_list_bunnies



matrix=[]
n,m=[int(x) for x in input().split()]
actual_row_player, actual_col_player=(0, 0)
start_bunny_coord=[]
for row in range(n):
    current_row=list(input())
    matrix.append(current_row)
    for col in range(len(current_row)):
        if current_row[col]=="P": # the blayer
            actual_row_player, actual_col_player=(row, col)
        if current_row[col]=="B": # the blayer
            start_bunny_coord.append((row, col))


comands_list=deque(list(input()))
dead=False
while comands_list:
    current_command=comands_list.popleft()
    next_row,next_col=directtions(current_command, actual_row_player, actual_col_player)
    if check_if_coord_outside(next_row,next_col,n,m): # he is outside
        matrix[actual_row_player][actual_col_player] = "."
        bunny_spreading(start_bunny_coord, matrix, n, m)
        break
    if matrix[next_row][next_col]=="B":
        matrix[actual_row_player][actual_col_player]="."
        matrix[next_row][next_col]="B"
        actual_row_player, actual_col_player = next_row, next_col
        bunny_spreading(start_bunny_coord, matrix, n, m)
        dead=True
        break
    if matrix[next_row][next_col]==".":
        matrix[next_row][next_col] = "P"
        matrix[actual_row_player][actual_col_player] = "."
        report_spread=bunny_spreading(start_bunny_coord, matrix, n, m)
        if report_spread=="died":
            dead=True
            break
        else:
            start_bunny_coord = report_spread
    actual_row_player, actual_col_player = next_row, next_col



print_matrix(matrix)

if dead:
    print(f"dead: {actual_row_player} {actual_col_player}")
else:
    print(f"won: {actual_row_player} {actual_col_player}")

