def print_matrix(mat):
    for each_row in mat:
        print(''.join(each_row))

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

size_of_matrix=int(input())
actual_row, actual_col=(0,0)
matrix=[]
burrows=[]
for row in range(size_of_matrix):
    current_row=list(input())
    matrix.append(current_row)
    for col in range(len(current_row)):
        if current_row[col]=="S":
            actual_row, actual_col=(row, col)
        if current_row[col]=="B":
            burrows.append((row, col))

food_quantity=0
game_over=False
while True:
    direction=input()
    next_row,next_col= directtions(direction,actual_row,actual_col)
    if check_if_coord_outside(next_row,next_col,size_of_matrix):
        matrix[actual_row][actual_col] = "."
        game_over=True
        break
    if matrix[next_row][next_col]=="*": # this is food
        food_quantity+=1
        matrix[next_row][next_col] ="S"
        matrix[actual_row][actual_col] ="."

    elif matrix[next_row][next_col]=="-" :# this is free
        matrix[next_row][next_col] = "S"
        matrix[actual_row][actual_col] = "."

    elif  matrix[next_row][next_col]=="." : # this is snake tail
        pass

    elif matrix[next_row][next_col]=="B": # this is burrows
        matrix[actual_row][actual_col] = "."
        matrix[next_row][next_col] = "."
        burrows.remove((next_row,next_col))
        actual_row, actual_col = burrows[0]
        continue
    actual_row, actual_col = next_row, next_col
    if food_quantity>=10:
        break


if game_over:
    print("Game over!")
else:
    print("You won! You fed the snake.")
print(f"Food eaten: {food_quantity}")
print_matrix(matrix)