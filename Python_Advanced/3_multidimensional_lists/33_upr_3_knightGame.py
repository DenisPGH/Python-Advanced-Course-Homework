

def Knight_moves(row:int,col:int):
    counter_range=0
    if 0 <= row - 2 < size_board and 0 <= col - 1 < size_board:
        if matrix[row - 2][col - 1] == "K":
            counter_range+=1
    if 0 <= row - 1 < size_board and 0 <= col - 2 < size_board:
        if matrix[row - 1][col - 2] == "K":
           counter_range += 1

    if 0 <= row - 2 < size_board and 0 <= col + 1 < size_board:
        if matrix[row - 2][col + 1] == "K":
            counter_range+=1
    if 0 <= row - 1 < size_board and 0 <= col + 2 < size_board:
        if matrix[row - 1][col + 2] == "K":
            counter_range+=1
    if 0 <= row + 1 < size_board and 0 <= col - 2 < size_board:
        if matrix[row + 1][col - 2] == "K":
            counter_range += 1
    if 0 <= row + 2 < size_board and 0 <= col - 1 < size_board:
        if matrix[row + 2][col - 1] == "K":
            counter_range+=1
    if 0 <= row + 2 < size_board and 0 <= col + 1 < size_board:
        if matrix[row + 2][col + 1] == "K":
            counter_range+=1
    if 0 <= row + 1 < size_board and 0 <= col + 2 < size_board:
        if matrix[row + 1][col + 2] == "K":
            counter_range+=1
    else:  # no knight in range
        pass
    return counter_range


size_board=int(input())
matrix=[]
# strore the matrix
for r in range(size_board):
    row_act=list(input())
    matrix.append(row_act)

# searching for K
removed_knight=0
store_Knights_range = {}
knight_for_remove=''
knight_row=-1
knight_col=-1
while True: # while is found

    #max_value=0
    knight_for_remove = ''
    knight_row = -1
    knight_col = -1
    store_Knights_range = {}
    for rr in range(size_board):
        max_value=0
        for c in range(size_board): # serch who knight how many horses can kill
            if matrix[rr][c] == "K":
                if Knight_moves(rr,c)>0:
                    store_Knights_range[(rr,c)]=Knight_moves(rr,c)

    # search the knight with most result
    if not store_Knights_range:
        break
    for knight, value in store_Knights_range.items():
        if value > max_value:
            max_value = value
            knight_for_remove = knight
            knight_row = knight[0]
            knight_col = knight[1]
    # remove the knights with the most result
    if store_Knights_range:  # if something is found
        del store_Knights_range[knight_for_remove]
        matrix[knight_row][knight_col] = 0
        removed_knight += 1




#print(f"{(store_Knights_range)}")
print(removed_knight)


#print the matrix
# for r in range(size_board):
#     print(*matrix[r],sep=" ")