def list_manipulator(list_,*args):
    def remove_(list_r,position,*args):
        if not args:
            list_r.pop(position)
        else:
            if len(args)==1:
                if position>=0:
                    list_r=list_r[args[0]:]
                else:
                    list_r = list_r[:-args[0]]

        return list_r


    def add_(list_a,position,*args):
        if position>=0:
            for each_ind in range(len(args)-1,-1,-1):
                value=args[each_ind]
                list_a.insert(position,value)
        else:
            for each_ind in range(len(args)):
                value=args[each_ind]
                list_a.append(value)

        return list_a

    position_dict={"beginning": 0,
                   "end" : -1}
    action_dict={"remove": remove_,
                 "add": add_}
    action=args[0]
    position=args[1]
    return action_dict[action](list_,position_dict[position],*args[2:])








# print(list_manipulator([1, 2, 3], "remove", "end")) # [1, 2]
# print(list_manipulator([1, 2, 3], "remove", "beginning")) # [2, 3]
# print(list_manipulator([1, 2, 3], "add", "beginning", 20)) # [20, 1, 2, 3]
# print(list_manipulator([1, 2, 3], "add", "end", 30))
# print(list_manipulator([1, 2, 3], "remove", "end", 2))# [1]
# print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
# print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
# print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
