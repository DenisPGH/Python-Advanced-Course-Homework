
def print_matrix(mat):
    for each_row in mat:
        print(' '.join(each_row))

def check_if_coord_outside(row,col,dimes):
    if row<0 or row >=dimes or col<0 or col>=dimes:
        return True
    else:
        return False

def directtions(richtung,row,col):
    if richtung=="up":
        return row-1,col
    if richtung=="down":
        return row + 1, col
    if richtung=="left":
        return row , col-1
    if richtung=="right":
        return row, col+1

matrix=[]
my_start_coord=(0,0)
all_targets=[]
hittet_targets=[]
for row in range(5):
    current_row=input().split()
    matrix.append(current_row)
    for col in range(len(current_row)):
        if current_row[col]=="A":
            my_start_coord=(row,col)
        if current_row[col]== "x" or current_row[col]== "X":
            all_targets.append((row,col))


comands_value=int(input())
curr_row, curr_col=my_start_coord
act_row,act_col=my_start_coord
current_place='.'
wrong_step=False
all_target_value=len(all_targets)
for com in range(comands_value):
    command=input()
    command_parts=command.split()
    action=command_parts[0]
    """•	"move {right/left/up/down} {steps}" – you should move in the given direction with the
     given steps. You can only move if the field you want to step on is marked with "."."""
    if action=="move":
        curr_row, curr_col= act_row, act_col
        direction=command_parts[1]
        steps=int(command_parts[2])
        while steps>0 :
            next_row, next_col = directtions(direction, curr_row, curr_col)
            if check_if_coord_outside(next_row, next_col, 5):
                wrong_step=True
                break
            if matrix[next_row][next_col]!= ".":
                matrix[curr_row][curr_col] = "A"
                break
            matrix[curr_row][curr_col]= "."
            matrix[next_row][next_col]= "A"
            steps-=1
            curr_row, curr_col= next_row, next_col

        act_row,act_col= curr_row, curr_col


    elif action== "shoot":
        direction = command_parts[1]
        curr_row, curr_col=act_row,act_col
        while all_targets:
            next_row, next_col = directtions(direction, curr_row, curr_col)
            if check_if_coord_outside(next_row, next_col, 5):
                #wrong_step = True
                break
            if matrix[next_row][next_col] == "x" or matrix[next_row][next_col] == "X":
                matrix[next_row][next_col]= "."
                hittet_targets.append((next_row, next_col))
                all_targets.remove((next_row, next_col))
                break
            curr_row, curr_col = next_row, next_col

        if len(all_targets)==0:
            break









if len(hittet_targets)==all_target_value:
    print(f"Training completed! All {len(hittet_targets)} targets hit.")
elif len(hittet_targets)<all_target_value or wrong_step:
    print(f"Training not completed! {len(all_targets)} targets left.")


for each in hittet_targets:
    print(list(each))





#print_matrix(matrix)
#print(act_row,act_col)