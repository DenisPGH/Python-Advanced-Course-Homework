sequence=input()
stack_list=[]
a=["()","{}","[]"]
wrong=False
for char in sequence:  # {[()]}    {[(])}
    if char in "{[(":
        stack_list.append(char)
    if char not in "{[(" and stack_list:
        if f"{stack_list[-1]}{char}" in a:
            stack_list.pop()
            wrong=True
        else:
            wrong = False
    else:
        wrong=False



if not wrong:
    print("NO")
else:
    print("YES")