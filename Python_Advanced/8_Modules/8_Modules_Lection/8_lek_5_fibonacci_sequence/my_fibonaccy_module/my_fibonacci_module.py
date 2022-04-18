def return_fibonaci(num):
    """ this function return the fibonaci as list"""
    sequence=[]
    for m in range(num):
        sequence.append(F(m))

    return sequence



def F(n):
    """ return a value of fibonaci for each number ,which we give"""
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)


#print(return_fibonaci(10))