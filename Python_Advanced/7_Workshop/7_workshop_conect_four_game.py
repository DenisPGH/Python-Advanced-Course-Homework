def print_matrix(ma):
    # this funcition print the matrix
    for row in  ma:
        print(row)

def make_move_function(ma, index_col, player, columns,rows):
    """  this function mark the filed for curent player"""
    index=index_col-1
    if 0<=index< columns : # if the index is valid
        index_row=-1
        while -1>= index_row>= -rows:
            if ma[index_row][index]==0: # if last down is free put mark there
                ma[index_row][index] = player

                return index_row,index_col # if the player made successed valid move

            else:
                index_row-=1
        print(f"Wrong choise player {player}, try again!")
        return False

    else:
        print(f"Wrong choise player {player}, try again!")
        return False

def prove_winner(ma,row,cow,max_col, max_row,player):
    """
    ERROR: when go up, give error be while loop, fixed with execption
    ERROR: when start from right-down occurce error, line 120 ===>> 7,6 ,6, fixed with exection

    this function, prove if there is 4 same numbers on line
    here I have to write the code , in all directions
    if nobody winn return tuple== -row,cow, else return "winn"
    """
    enought = False
    winn = False
    """   prove horizontal """
    index_value = 0
    counter_player = 0
    # go left
    while ma[row][(cow - index_value)-1] == player \
            and 0 <= (cow - index_value)-1 < max_col and -1>=row>=-max_row :
        if ma[row][(cow - index_value)-1] == player:  # if is same player go on
            counter_player += 1
            if counter_player ==4:  # if has 4 same
                counter_player=0
                winn = True
                break
        index_value+=1
    # go right
    index_value = 1
    if  -1>=row>=-max_row and 0 <= (cow + index_value)-1 < max_col:
        while ma[row][(cow + index_value)-1] == player:
            if ma[row][(cow + index_value)-1] == player:  # if is same player go on
                counter_player += 1
                if counter_player ==4:  # if has 4 same
                    counter_player=0
                    winn = True
                    break
            index_value+=1
    counter_player = 0 # make zero again before naxt line
    index_value = 0
    """   prove vertical """
    while ma[row+index_value][cow-1] == player and 0 <= cow-1 < max_col and -1>=row+index_value>=-max_row :
        if ma[row+index_value][cow -1] == player:  # if is same player go on
            counter_player += 1
            if counter_player ==4:  # if has 4 same
                counter_player=0
                winn = True
                break
        index_value+=1

    """   prove diagonal left-down <<>> right-up"""
    counter_player = 0  # make zero again before naxt line
    index_value = 0
    # profe upstairs right
    if -1>=row+index_value>=-max_row and 0 <= cow-1-index_value < max_col:
        while ma[(row)+index_value][(cow-1)-index_value] == player:
            if ma[row + index_value][(cow-1)-index_value] == player:  # if is same player go on
                counter_player += 1
                if counter_player == 4:  # if has 4 same
                    counter_player = 0
                    winn = True
                    break
            index_value += 1
    # prove downstairs left
    index_value = 1
    if -1>=row-index_value>=-max_row and 0 <= cow-1+index_value < max_col:
        try:
            while ma[(row)-index_value][(cow-1)+index_value] == player:
                if ma[row - index_value][(cow-1)+index_value] == player:  # if is same player go on
                    counter_player += 1
                    if counter_player == 4:  # if has 4 same
                        counter_player = 0
                        winn = True
                        break
                index_value += 1
        except IndexError:
            pass
    """  prove diagonal right-down <<<>>> left-up"""
    counter_player = 0  # make zero again before naxt line
    index_value = 0
    # profe upstairs left
    if -1 >= (row-index_value) >= -max_row and 0 <= ((cow - 1)-index_value)  < max_col:
        try:
            while ma[(row-index_value)][(cow - 1) - index_value] == player:
                if ma[row - index_value][(cow - 1) - index_value] == player:  # if is same player go on
                    counter_player += 1
                    if counter_player == 4:  # if has 4 same
                        counter_player = 0
                        winn = True
                        break
                index_value += 1
        except IndexError:
            pass
    ## prove downstairs right
    index_value = 1
    if -1 >= row + index_value > -max_row and 0 <= cow - 1 + index_value < max_col:
        try:
            while ma[row + index_value][(cow - 1) + index_value] == player\
                    and -1 >= row + index_value > -max_row and 0 <= cow - 1 + index_value < max_col:
                if ma[row + index_value][(cow - 1) + index_value] == player:  # if is same player go on
                    counter_player += 1
                    if counter_player == 4:  # if has 4 same
                        counter_player = 0
                        winn = True
                        break
                index_value += 1
        except IndexError:
            pass



    # after all check
    if winn:
        return "winn"
    else:
        return -row,cow # have to be with minus, because is first, from down to up





#### START ACTION ####
matrix_col=7
matrix_row=6
wishes_lenght=4
# create the matrix
matrix= [[0 for col in range(matrix_col)] for row in range(matrix_row)]

print_matrix(matrix)
counter=1
# while until someone winn
while True:
    parity= 2 if counter%2==0 else 1
    take_index=int(input(f"Player {parity}, please choose a column:  "))
    # string from the function
    message=make_move_function(matrix, take_index, parity, matrix_col, matrix_row)
    if type(message)==tuple:  # if function return tuple, this is the coodr of the player
        curent_row, current_col=message
        # hier we have to prove , if someone is winn the game
        status=prove_winner(matrix,curent_row,current_col,matrix_col,matrix_col,parity)
        if status== "winn":
            print_matrix(matrix)
            print(f"Player {parity} wonn the game!!")
            break
        else:
            print("")

    else: # if returns False, wrong choise, same player again
        continue
    # print the matrix every time
    print_matrix(matrix)
    counter+=1