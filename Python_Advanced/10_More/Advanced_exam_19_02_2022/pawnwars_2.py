def check_diagonal_for_enemy(mat,player:str,row,col):
    emeny= 'b' if player=='w' else 'w'
    if not check_if_player_outside(row - 1, col - 1) and player== 'w':
        if mat[row-1][col-1]==emeny:
            mat[row - 1][col - 1]=player
            mat[row ][col ] = '-'
            return True

    if not check_if_player_outside(row - 1, col + 1) and player== 'w':
        if mat[row-1][col+1]==emeny:
            mat[row][col] = '-'
            mat[row - 1][col +1]=player
            return True

    if not check_if_player_outside(row + 1, col + 1) and player== 'b':
        if mat[row+1][col+1]==emeny:
            mat[row][col] = '-'
            mat[row + 1][col +1]=player
            return True

    if not check_if_player_outside(row + 1, col - 1) and player== 'b':
        if mat[row + 1][col - 1] == emeny:
            mat[row][col] = '-'
            mat[row + 1][col - 1] = player
            return True









def check_if_player_outside(row, col):
    if not 0<= row<8 or not 0<=col<8:
        return True
    return False


def move_forward(player:str,row,col):
    if player=='w':
        return row-1,col
    elif player=='b':
        return row+1,col

    #return row,col




def print_matrix(mat):
    for each_row in mat:
        print(' '.join(each_row))

matrix=[]
collumn_to_alpha={0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h','w':'White','b':'Black'}
rows_to_num={0:8,1:7,2:6,3:5,4:4,5:3,6:2,7:1}
w=(0,0)
b=(0,0)
for a in range(8):
    row=input().split(" ")
    matrix.append(row)
    for each in range(len(row)):
        if row[each]=='w':
            w=a,each
        if row[each] == 'b':
            b= a, each

#print(w)
#print(b)

w_cur_row,w_cur_col=w
b_cur_row,b_cur_col=b
winner=''
final_row=""
final_col=""
got_it=False
counter=0
while True:
    if counter %2==0:
        w_next_row,w_next_col=move_forward("w",w_cur_row,w_cur_col)
        if check_if_player_outside(w_next_row, w_next_col):
            final_row,final_col=w_cur_row, w_cur_col
            winner='w'
            break
        elif  check_diagonal_for_enemy(matrix,"w",w_cur_row,w_cur_col) :
            final_row, final_col = b_cur_row, b_cur_col
            winner = 'w'
            got_it = True
            break
        else:
            matrix[w_cur_row][w_cur_col] = '-'
            matrix[w_next_row][w_next_col] = 'w'
        w_cur_row, w_cur_col = w_next_row, w_next_col


    else:
        b_next_row, b_next_col = move_forward("b", b_cur_row, b_cur_col)
        if check_if_player_outside(b_next_row, b_next_col) :
            final_row, final_col = b_cur_row, b_cur_col
            winner = 'b'
            break
        elif check_diagonal_for_enemy(matrix,"b",b_cur_row,b_cur_col):
            final_row, final_col = w_cur_row, w_cur_col
            winner = 'b'
            got_it = True
            break
        else:
            matrix[b_cur_row][b_cur_col] = '-'
            matrix[b_next_row][b_next_col] = 'b'
        b_cur_row, b_cur_col = b_next_row,b_next_col
    counter+=1

    #print("=================")
    #print_matrix(matrix)

if not got_it:
    print(f"Game over! {collumn_to_alpha[winner]} pawn is promoted to a queen at"
          f" {f'{collumn_to_alpha[final_col]}{rows_to_num[final_row]}'}.")

else:
    print(f"Game over! {collumn_to_alpha[winner]} win, capture on"
          f" {f'{collumn_to_alpha[final_col]}{rows_to_num[final_row]}'}.")

