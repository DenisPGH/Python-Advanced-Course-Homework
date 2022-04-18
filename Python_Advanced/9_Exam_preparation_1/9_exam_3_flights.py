def flights(*args):
    dict_args={}
    counter=0
    for each_ind in range(len(args)):
        if args[each_ind]=="Finish":
            break
        elif counter%2==0:
            if args[each_ind] not in dict_args:
                dict_args[args[each_ind]]=args[each_ind+1]
            else:
                dict_args[args[each_ind]] += args[each_ind + 1]

        counter+=1
    return dict_args





# print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
#
# print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
#
# print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))