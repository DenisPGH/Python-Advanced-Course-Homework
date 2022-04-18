def add_(a,b):
    return a+b


def subtract_(a,b):
    return a-b


def po_(a,b):
    return a*b


def divide_(a,b):
    if b !=0:
        return a/b
    else:
        return "The number cant divide by zero!"


def pow_(a,b):
    return a**b




def operation(a:float,sign:str,b:int):
    if sign in signs_dict:
        return f"{signs_dict[sign](a,b):.2f}"
    else: # wrong mathematical sign
        return "Invalid sign."



signs_dict={
    "+": add_,
    "-": subtract_,
    "*": po_,
    "/": divide_,
    "^": pow_,
}

#print(operation(5,"^",2))