from collections import deque
# 5 6
# SoftUni

# 1 5
# Denis
empty_deque=deque()
row, col =[int(x) for x in input().split()]
snake=input()
matrix=[]
cur_word=deque(snake)
for r in range(row):
    matrix.append(deque())
    for c in range(col):
        if r%2==0: # even goes left-right
           if len(cur_word)>0:
               matrix[r].append(cur_word.popleft())
           else:
               cur_word=deque(snake)
               matrix[r].append(cur_word.popleft())
        else:  # goes right-left
            if len(cur_word) > 0:
                matrix[r].appendleft(cur_word.popleft())
            else:
                cur_word = deque(snake)
                matrix[r].appendleft(cur_word.popleft())

        # else: # goes right-left
        #     if c<len(snake):
        #        matrix[r].append(snake[(len(snake)-r)-c])
        #         #matrix[r].append(snake[c])
        #     else:
        #         matrix[r].append(snake[c - (len(snake) - r)])

for a in range(row):
    print(''.join(matrix[a]))

