text=input()
stack_list=[]
start_index=0
for index in range(len(text)):
    if text[index]=="(":
        stack_list.append(index)


    elif text[index]==")":
        start_index=stack_list.pop()
        print(text[start_index:index+1])
