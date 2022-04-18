import numbers


def print_matrix(mat):
    for each_row in mat:
        print(' '.join(each_row))

def check_if_coord_outside(row,col,dimes):
    if row<0 or row >=dimes or col<0 or col>=dimes:
        return True
    else:
        return False

def finding_coresponding_numbers(row, col, mat, value_mul):
    total_sum_points=0
    counter_step=1
    while True:  #go up
        current_cell=mat[row - counter_step][col]
        if current_cell.isdigit():
            total_sum_points+=int(current_cell)
            counter_step=1
            break
        else:
            counter_step+=1
    while True:  #go down
        current_cell=mat[row + counter_step][col]
        if current_cell.isdigit():
            total_sum_points += int(current_cell)
            counter_step=1
            break
        else:
            counter_step+=1
    while True:  #go left
        current_cell=mat[row ][col - counter_step]
        if current_cell.isdigit():
            total_sum_points += int(current_cell)
            counter_step=1
            break
        else:
            counter_step+=1

    while True:  #go right
        current_cell=mat[row ][col + counter_step]
        if current_cell.isdigit():
            total_sum_points += int(current_cell)
            counter_step=1
            break
        else:
            counter_step+=1

    return total_sum_points *value_mul





name_a,name_b=input().split(", ")
dict_players={ f"{name_a}": {"start_p":501, "throws": 0},
               f"{name_b}": {"start_p":501, "throws": 0}}
matrix=[]
for row in range(7):
    current_row=input().split()
    matrix.append(current_row)
counter=0
current_player=''
while True:
    row,col=eval(input())
    if check_if_coord_outside(row,col,7): # trow outside
        counter += 1
        continue
    current_target=matrix[row][col]
    current_player= name_a if counter %2==0 else name_b
    dict_players[current_player]["throws"] += 1

    if current_target.isdigit(): # he hits number
        current_target=int(current_target)
        dict_players[current_player]["start_p"]-=current_target
    elif current_target=="D":
        reduce=finding_coresponding_numbers(row,col,matrix,2)
        dict_players[current_player]["start_p"]-=reduce
    elif current_target=="T":
        reduce = finding_coresponding_numbers(row, col, matrix, 3)
        dict_players[current_player]["start_p"] -= reduce
    elif current_target=="B":
        break
    if dict_players[current_player]["start_p"]<=0:
        break


    counter+=1



#print_matrix(matrix)
print(f"{current_player} won the game with {dict_players[current_player]['throws']} throws!")

