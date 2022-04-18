import numbers


def fill_the_box(heigh,lenght,width,*args):
    size_box=heigh*lenght*width
    capazitet=size_box
    all_count_items=0
    filled_items=0
    for each in args:
        if each !="Finish":
            all_count_items+=each
        elif each =="Finish":
            break

    for each in args:
        if isinstance(each,numbers.Number):
            if size_box-each>=0:
                size_box-=each
                filled_items+=each
            else:
                return  f"No more free space! You have {all_count_items-capazitet} more cubes."
        else:
            if size_box>=0:
                return f"There is free space in the box. You could put {size_box} more cubes."
            else:
                return f"No more free space! You have {all_count_items-capazitet} more cubes."


# print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
#
# # There is free space in the box. You could put 13 more cubes.
#
# print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
#
# print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))