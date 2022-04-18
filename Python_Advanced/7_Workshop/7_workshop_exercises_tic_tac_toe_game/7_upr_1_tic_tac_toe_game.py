def print_board(ma):
    """ just print the given matrix"""
    for a in ma:
        print("| ", end="")
        print(" | ".join([str(x) for x in a]),end="")
        print(" |")

def return_coord_of_choose(ma, dim, choise):
    """ return exaclty coordinates by given index , if index is in range-return exactly coordinates,
     else return big number to activate wrong message"""
    for row in range(dim):
        for col in range(dim):
            if ma[row][col]==choise:
                return row,col
    return 10,10 # by wrong above 9

def start_setup(ma, dimension):
    """ This function start the program
    player names, player signs, and board with the numbers of field for play"""
    global player_one, player_two,matrix, player_dict

    player_one=input("Player one name: ")
    player_two=input("Player two name: ")
    player_one_sign=input(f"{player_one} would you like to play with 'X' or 'O' ?")
    chosen_already= "X" if player_one_sign=='O' else "O"
    player_dict={player_one:player_one_sign,player_two:chosen_already}
    print(f"Then {player_two} play with {chosen_already}")
    print("This is numeration on the board:")
    m=1
    for row in range(1,dimension+1):
        for col in range(1,dimension+1):
            ma[row-1][col-1]=m
            m+=1
    print_board(ma)
    #matrix=ma.copy()
    print(f"{player_one} starts first.")

def making_changes_on_the_table(dim,table, choose_row,choose_col,player, dict):
    """ this function mark every new move for the player, by wrong index return 'wrong index'
    by index with alredy market return again
    by success index retrun the table with the changes"""
    # making right chooise
    if 0<=choose_row < dim and 0<=choose_col< dim:
        if table[choose_row][choose_col]==' ': # if field is free
            table[choose_row][choose_col] = dict[player]
        else: # if field is with signt
            return "again"
    else: # if index is wrong
        return "wrong index"

    return table # if it was right


def prove_for_winner(ma, row, col, max_col, max_row, sign, how_much):
    """
    this function, prove if there is 3 same numbers on line in all directions
    it works line by line , if there is a 3 same on some line return true, else false

    """
    player=player_dict[sign]
    enought = False
    winn = False
    """   prove horizontal """
    index_value = 0
    counter_player = 0
    # go left
    while ma[row][col - index_value] == player \
            and 0 <= col-index_value < max_col and 0<=row<max_row :
        if ma[row][col - index_value] == player:  # if is same player go on
            counter_player += 1
            if counter_player ==how_much:  # if has 4 same
                counter_player=0
                winn = True
                break
        index_value+=1
    # go right
    index_value = 1
    if  0<=row<max_row and 0 <= (col + index_value)< max_col:
        try:
            while ma[row][(col + index_value)] == player:
                if ma[row][(col + index_value)] == player:  # if is same player go on
                    counter_player += 1
                    if counter_player ==how_much:  # if has 4 same
                        counter_player=0
                        winn = True
                        break
                index_value+=1
        except IndexError:
            pass
    counter_player = 0 # make zero again before naxt line
    index_value = 0
    """   prove vertical """
    # go down
    try:
        while ma[row+index_value][col] == player and 0 <= col < max_col and 0<=row+index_value<max_row :
            if ma[row+index_value][col] == player:  # if is same player go on
                counter_player += 1
                if counter_player ==how_much:  # if has 4 same
                    counter_player=0
                    winn = True
                    break
            index_value+=1
    except IndexError:
        pass
    index_value = 1
    # go up
    try:
        while ma[row-index_value][col] == player and 0 <= col < max_col and 0<=row-index_value<max_row :
            if ma[row-index_value][col] == player:  # if is same player go on
                counter_player += 1
                if counter_player ==how_much:  # if has 4 same
                    counter_player=0
                    winn = True
                    break
            index_value+=1
    except IndexError:
        pass

    """   prove diagonal left-down <<>> right-up"""
    counter_player = 0  # make zero again before naxt line
    index_value = 0
    # profe upstairs right
    if 0<=row-index_value<max_row and 0 <= col+index_value < max_col:
        try:
            while ma[row-index_value][col + index_value] == player:
                if ma[row - index_value][col + index_value] == player:  # if is same player go on
                    counter_player += 1
                    if counter_player == how_much:  # if has 4 same
                        counter_player = 0
                        winn = True
                        break
                index_value += 1
        except IndexError:
            pass
    # prove downstairs left
    index_value = 1
    if 0<=row+index_value<max_row and 0 <= col-index_value < max_col:
        try:
            while ma[row+index_value][col - index_value] == player:
                if ma[row+index_value][col - index_value] == player:  # if is same player go on
                    counter_player += 1
                    if counter_player == how_much:  # if has 4 same
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
    if 0<=row-index_value<max_row and 0 <= (col - index_value) < max_col:
        try:
            while ma[row-index_value][col - index_value] == player:
                if ma[row - index_value][col - index_value] == player:  # if is same player go on
                    counter_player += 1
                    if counter_player == how_much:  # if has 4 same
                        counter_player = 0
                        winn = True
                        break
                index_value += 1
        except IndexError:
            pass
    ## prove downstairs right
    index_value = 1
    if 0<=row+index_value<max_row and 0 <= col+index_value < max_col:
        try:
            while ma[row + index_value][col + index_value] == player\
                    and 0<=row+index_value<max_row and 0 <= col+ index_value < max_col:
                if ma[row + index_value][col + index_value] == player:  # if is same player go on
                    counter_player += 1
                    if counter_player == how_much:  # if has 4 same
                        counter_player = 0
                        winn = True
                        break
                index_value += 1
        except IndexError:
            pass

    counter_player = 0
    # after all check
    if winn:
        return True
    else:
        return False # have to be with minus, because is first, from down to up

def is_draw(ma,range_col, range_row):
    """ if all full return true, else false"""
    for r in range(range_row):
        if not all([x != " " for x in ma[r]]):
            return False
    else:
        return True




"""  HIER START THE CODE"""
player_dict={} # store the players and their signs
player_one=None
player_two=None
dimensions=3 # dimension of the field
wish=3 # how much same signs on line we want
matrix=[[" " for x in range(dimensions)] for j in range(dimensions)] # matrix with the number for marking
play_table=[[" " for x in range(dimensions)] for j in range(dimensions)] # real table for play


start_setup(matrix, dimensions)
counter=0





while True:
    if counter >100: # this can be remove, only 100 moves
        break
    parity= player_one if counter%2==0 else player_two
    # wait the curent player to make choise
    choise_current_player= int(input(f"{parity} choose a free position [1-9]: "))
    # got the coordinates of the chosen place
    player_row, player_col= return_coord_of_choose(matrix, dimensions, choise_current_player)

    # make the changes on the table
    actual_table=making_changes_on_the_table(dimensions,play_table,player_row,player_col,parity,player_dict)
    if type(actual_table)==str:
        if actual_table =="again":
            print(f"{parity} choose a new position, this is marked: ")
        elif actual_table== "wrong index":
            print(f"{parity} choose a valid position 1-9: ")
        continue
    else:
    # print every time the result
        print_board(actual_table)
    #### HIER HAVE TO PROVE EVERY TIME , IF SOMEONE WINN ####
        if prove_for_winner(actual_table, player_row, player_col, dimensions, dimensions, parity, wish):
            print(f"{parity} won!!!")
            break
        # check if all fields are full, but not with winner
        elif is_draw(actual_table,dimensions,dimensions):
            print("Draw!")
            break

    counter+=1