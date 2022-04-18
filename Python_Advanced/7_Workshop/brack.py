# while True:
#     index_value = 0
#     counter_player=0
#     while ma[row][cow+index_value] ==player and 0<= ma[row][cow+index_value]<max_col : # go right
#         if ma[row][cow+index_value]==player: # if is same player go on
#             counter_player+=1
#             if counter_player==4: # if has 4 same
#                 enought=True
#                 break
#         else: # not same player
#             index_value = 0
#             break
#         index_value += 1
#     while ma[row][cow-index_value] ==player and 0<= ma[row][cow-index_value]<max_col: # go left
#         if ma[row][cow-index_value]==player:
#             counter_player+=1
#             if counter_player==4:
#                 enought=True
#                 break
#         else:
#             break
#         index_value += 1
#     if enought: # if has 4 same
#         winn=True
#         break
#     else: # no more indexes
#         break


# if return_current_indexes_of_the_plaeyer(ma,player,columns,rows,index_row,index_col):  # the move was success
                #     print(f"winner is {player}")
                #     return "winn"
                # else:
                #     print(f"player {player} made valid move")
                #     return True


# def return_current_indexes_of_the_plaeyer(ma,player,max_col, max_row,row_player,col_player):
#     if -row_player>4:
#         return True
#     else:
#         return False



#take_index=int(input())

    # if wrong move is made retrun false, the player must make step again
    # if make_move_function(matrix, take_index, parity, matrix_col, matrix_row) \
    #         or make_move_function(matrix, take_index, parity, matrix_col, matrix_row)=="winn":
    #     # hier we have to prove every time, if someone is winn the game
    #     #prove_winner(matrix,)
    #     print()
counter=0
if counter > 1000:  # break after 10 turns, this is not need, just some end of game
    #break