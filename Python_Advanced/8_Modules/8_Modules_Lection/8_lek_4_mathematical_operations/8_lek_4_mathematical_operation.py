from math_operation_module.math_operation_module import operation as op

text=input()
first_num,sign,second_num=text.split()
print(op(float(first_num),sign,int(second_num)))