"""•	On the first line, you are given the integer m - the count of presents
•	On the second - integer n - the size of the neighborhood
•	The following n lines hold the values for every row
•	On each of the following lines you will get a command
"""

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

def coocies(row,col,mat,dim,count_presents):
    counter_gived_presents=0
    nice_kid=0
    if not check_if_coord_outside(row-1,col,dim) :
        if mat[row-1][col]=="V":
            counter_gived_presents+=1
            nice_kid+=1
            count_presents-=1
            mat[row - 1][col] ="-"
        if mat[row-1][col]=="X":
            counter_gived_presents += 1
            mat[row - 1][col] = "-"
            count_presents -= 1
        if count_presents==0:
            return counter_gived_presents,nice_kid

    if not check_if_coord_outside(row+1,col,dim):
        if mat[row + 1][col] == "V":
            counter_gived_presents += 1
            nice_kid += 1
            count_presents -= 1
            mat[row + 1][col] = "-"
        if mat[row + 1][col] == "X":
            counter_gived_presents += 1
            count_presents -= 1
            mat[row + 1][col] = "-"
        if count_presents==0:
            return counter_gived_presents,nice_kid
    if not check_if_coord_outside(row,col-1,dim):
        if mat[row ][col-1] == "V":
            counter_gived_presents += 1
            nice_kid += 1
            count_presents -= 1
            mat[row ][col- 1] = "-"
        if mat[row ][col- 1] == "X":
            counter_gived_presents += 1
            count_presents -= 1
            mat[row ][col- 1] = "-"
        if count_presents==0:
            return counter_gived_presents,nice_kid
    if not check_if_coord_outside(row,col+1,dim):
        if mat[row ][col+1] == "V":
            counter_gived_presents += 1
            count_presents -= 1
            nice_kid += 1
            mat[row ][col+1] = "-"
        if mat[row ][col+1] == "X":
            counter_gived_presents += 1
            count_presents -= 1
            mat[row][col+1] = "-"
        if count_presents==0:
            return counter_gived_presents,nice_kid

    return counter_gived_presents,nice_kid

count_of_presents=int(input())
size_of_matrix=int(input())
matrix=[]
actual_row, actual_col=(0, 0)
nice_kid_value=[]
# X -bad kid, V- good kid, C- cookies   , - empty
for row in range(size_of_matrix):
    current_row=input().split()
    matrix.append(current_row)
    for col in range(len(current_row)):
        if current_row[col]=="S":
            actual_row, actual_col=(row, col)
        if current_row[col]== "V":
            nice_kid_value.append((row,col))

run_out_present=False
counter_gived_presents_to_good_kids=0
while True:
    command=input()
    if command== "Christmas morning":
        break
    next_row,next_col=directtions(command,actual_row,actual_col)
    if check_if_coord_outside(next_row, next_col, size_of_matrix):
        break
    if matrix[next_row][next_col]== "V":
        count_of_presents-=1
        matrix[next_row][next_col] ="S"
        matrix[actual_row][actual_col] ="-"
        counter_gived_presents_to_good_kids+=1

    elif matrix[next_row][next_col]== "X":
        matrix[next_row][next_col] = "S"
        matrix[actual_row][actual_col] = "-"

    elif matrix[next_row][next_col]== "C":
        matrix[next_row][next_col] = "S"
        matrix[actual_row][actual_col] = "-"
        a,b =coocies(next_row,next_col,matrix,size_of_matrix,count_of_presents)
        count_of_presents -=a
        counter_gived_presents_to_good_kids+=b
    else:
        matrix[next_row][next_col] = "S"
        matrix[actual_row][actual_col] = "-"


    if count_of_presents<=0 and len(nice_kid_value)>counter_gived_presents_to_good_kids:
        run_out_present=True
        break
    if len(nice_kid_value)==counter_gived_presents_to_good_kids and count_of_presents==0:
        break

    actual_row,actual_col=next_row,next_col




#print(count_of_presents)

if run_out_present :
    print("Santa ran out of presents!")
print_matrix(matrix)
if not run_out_present and len(nice_kid_value)==counter_gived_presents_to_good_kids:
    print(f"Good job, Santa! {counter_gived_presents_to_good_kids} happy nice kid/s.")
else:
    print(f"No presents for {len(nice_kid_value)-counter_gived_presents_to_good_kids} nice kid/s.")