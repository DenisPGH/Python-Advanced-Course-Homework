def triangle_function(n):
    """ n is the end value of my triangle"""
    for a in range(1,n+1):
        for b in range(1,a+1):
           print(b,end=" ")
        print()

    for c in range(n-1,-1,-1):
        for d in range(1,c+1):
            print(d,end=" ")
        print()


# triangle_function(4) # for prove the result