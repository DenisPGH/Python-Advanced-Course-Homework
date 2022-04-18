class ValueCannotBeNegative(Exception):
    pass

for a in range(5):
        number=int(input())
        if number<0:
            raise ValueCannotBeNegative()






