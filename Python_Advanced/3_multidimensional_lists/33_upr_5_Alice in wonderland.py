dimensions_field=int(input())
matrix=[]
def print_matrix(mat):
    for each_row in mat:
        print(' '.join(each_row))

def directtions(richtung,row,col):
    if richtung=="up":
        return row-1,col
    if richtung=="down":
        return row + 1, col
    if richtung=="left":
        return row , col-1
    if richtung=="right":
        return row, col+1

def check_if_coord_outside(row,col,dimes):
    if row<0 or row >=dimes or col<0 or col>=dimes:
        return True
    else:
        return False

alice_start_coord=(0,0)
alice_balance=0
for row in range(dimensions_field):
    current_row=input().split()
    matrix.append(current_row)
    for col in range(len(current_row)):
        if current_row[col]=="A":
            alice_start_coord=(row,col)
a_row,a_col=alice_start_coord
matrix[a_row][a_col]="*"
wrong_step=False
while True:
    direction=input()
    cur_row, cur_col=directtions(direction, a_row, a_col)
    if check_if_coord_outside(cur_row, cur_col, dimensions_field):
        wrong_step=True
        break
    current_place=matrix[cur_row][cur_col]
    if current_place.isdigit():
        alice_balance+=int(current_place)
    matrix[cur_row][cur_col]="*"
    if alice_balance >=10:
        break
    if current_place=="R":
        wrong_step=True
        break

    a_row,a_col=cur_row,cur_col





if alice_balance>=10:
    print("She did it! She went to the party.")

if wrong_step:
    print(f"Alice didn't make it to the tea party.")


print_matrix(matrix)


