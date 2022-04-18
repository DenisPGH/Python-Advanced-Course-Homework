
def sum_numbers(num1, num2):
    global x
    x =num1 + num2
    return x

def multiply_numbers(num1, num2):
    global z
    z=num1 * num2
    return z
# NE RABOTI TOZI VARIANT
# def func_executor(*args):
#     end_list = []
#     final=[]
#     for a in args:
#         result = 0
#         if a[0] == sum_numbers:
#             result= sum_numbers(a[1][0],a[1][1])
#         elif a[0] == multiply_numbers:
#             result=multiply_numbers(a[1][0],a[1][1])
#         end_list.append(result)
#     final.extend(end_list)
#     #return end_list # the result is lost?! when the end_list is outside is ok recursion?
#
#     return final
# AssertionError: Lists differ: [] != [3, 8]
#
# Second list contains 2 additional elements.
# First extra element 0:
# 3
#
# - []
# + [3, 8]




#AssertionError: Lists differ: [0, 0] != [3, 8]

# First differing element 0:
# 0
# 3
#
# - [0, 0]
# + [3, 8]

def func_executor(*args):
    end_list = []
    for funk,param in args: # tuple with tuples
        result = funk(*param)
        end_list.append(result)
    return end_list

print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))


