def sort_numbers(command,*args):
    odd_nums_sum=0
    odd_list=[]
    even_list=[]
    even_nums_sum=0
    result=""
    value=0
    for n in range(len(args)):
        for num in args[n]:
            if num %2 !=0: #odd
                odd_nums_sum+=num
                odd_list.append(num)
            else:
                even_nums_sum+=num
                even_list.append(num)
    even_list
    a=len(even_list)+len(odd_list)
    if command=="Odd":
        value=odd_nums_sum * a
    elif command=="Even":
        value=even_nums_sum*a

    return value





action=input() # "Odd" or "Even".
numbers=[int(x) for x in input().split()]
print(sort_numbers(action,numbers))