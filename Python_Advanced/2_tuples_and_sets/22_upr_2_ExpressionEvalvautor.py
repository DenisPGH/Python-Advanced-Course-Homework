# 6 3 - 2 1 * 5 /
from collections import deque

sequence= deque(input().split()) # 6 3 - 2 1 * 5 /     # 6 -3 - 2 1 * 5 /
signs=["+","-","*","/"]
final_sum_of_nums="a"
current_numbers_deq=deque()
#current_sum_nums = 0
for char in sequence:

   # print(char)
    if char in signs: # char is  / + - *
        if current_numbers_deq and final_sum_of_nums=="a": # i ako e pyrvo
            final_sum_of_nums = current_numbers_deq.popleft()
        if char == "+":
            while current_numbers_deq:
                final_sum_of_nums += current_numbers_deq.popleft()  # add the result to final

        elif char== "-":
            while current_numbers_deq:
                final_sum_of_nums -= current_numbers_deq.popleft()
        elif char == "*":
            while current_numbers_deq:
                final_sum_of_nums *= current_numbers_deq.popleft()
        elif char == "/": # divide to integer //
            while current_numbers_deq:
                final_sum_of_nums = final_sum_of_nums // current_numbers_deq.popleft()
       # print(final_sum_of_nums)
    else:  # if digite store in colectin
        current_numbers_deq.append(int(char))


print(final_sum_of_nums)

