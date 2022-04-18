def even_odd(*args):
    comand=args[-1]

    even_list=[]
    odd_list=[]
    result=''
    for a in args[:-1]:
        if a % 2==0: # even
            even_list.append(a)
        else:
            odd_list.append(a)
    if comand == "even":
        result= even_list
    elif comand=="odd":
        result= odd_list

    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))	# [2, 4, 6]
#print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))	# [1, 3, 5, 7, 9]
