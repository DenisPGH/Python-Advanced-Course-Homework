"""•	The first element should be added to the value of the key "a"
•	The second element should be subtracted from the value of the key "s"
•	The third element should be divisor to the value of the key "d"
•	The fourth element should be multiplied by the value of the key "m"
•	Each result should replace the value of the corresponding key
•	You must repeat the same steps consecutively until you run out of numbers
You cannot divide by 0
"""



def math_operations(*args,**kwargs):
    counter=1
    for index in range(len(args)):
        if counter==1:
            kwargs["a"]+=args[index]
        elif counter==2:
            kwargs["s"] -= args[index]
        elif counter==3:
            if args[index] !=0:
                kwargs["d"] /= args[index]
        elif counter==4:
            kwargs["m"] *= args[index]
        counter+=1
        if counter>4:
            counter=1

    return kwargs




# print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
#
# # {'a': 9, 's': 15, 'd': -3.0, 'm': -45}
#
# print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
#
# print(math_operations(6, a=0, s=0, d=0, m=0))