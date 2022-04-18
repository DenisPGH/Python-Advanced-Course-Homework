def operate(sign,*args):
    result=args[0]
    if sign=="+":
        for el in args[1:]:
            result+=el
    elif sign=="-":
        for el in args[1:]:
            result-=el
    elif sign=="*":
        for el in args[1:]:
            if el==0:
                continue
            else:
                result*=el
    elif sign=="/":
        for el in args[1:]:
            if el ==0:
                continue

            else:
                result /= el

    return result



#print(operate("+", 1, 2.0, 3))
#print(operate("*", 3, 4))
#print(operate("/", 32, 4,0,2))
#print(operate("-", 3, 4,5,6,7))