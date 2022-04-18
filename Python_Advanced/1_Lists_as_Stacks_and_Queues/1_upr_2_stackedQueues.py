# You have an empty stack. You will receive an integer – N. On the next N lines, you will receive queries. Each query is one of these four types:
# •	'1 {number}' – push the number (integer) into the stack
# •	'2' – delete the number at the top of the stack
# •	'3' – print the maximum number in the stack
# •	'4' – print the minimum number in the stack
# It is guaranteed that each query is valid.
# After you go through all the queries, print the stack from top to bottom in the following format:
number_lines=int(input())
stack_list=[]
for l in range(number_lines):
    line=input()
    line_info=line.split()
    comand=line_info[0]
    if comand=="1":
        num=int(line_info[1])
        stack_list.append(num)
    elif stack_list:
        if comand=="2":
            stack_list.pop()
        elif comand=="3":
            print(max(stack_list))
        elif comand=="4":
            print(min(stack_list))
while stack_list:
    if len(stack_list) >1:
        print(stack_list.pop(), end=", ")
    else:
        print(stack_list.pop())

