# The function should return the cheeses and their pieces' quantities
# sorted by the number of pieces of a cheese kind in descending order.
# If two or more cheeses have the same number of pieces,
# sort them by their names in ascending order (alphabetically).
# For each kind of cheese, return their pieces quantities in descending order.
# For more clarifications, see the examples below.
def sorting_cheeses(**kwargs):
    result=''
    for name,pieces in sorted(kwargs.items(),key= lambda x:(-len(x[1]),x[0])):
        result+=name+"\n"
        for p in sorted(pieces, key=int, reverse=True):
            result+=str(p)+'\n'


    return result



# print(
#     sorting_cheeses(
#         Parmesan=[102, 120, 135],
#         Camembert=[100, 100, 105, 500, 430],
#         Mozzarella=[50, 125],
#     )
# )
# Camembert\n500\n430\n105\n100\n100\nParmesan\n135\n120\n102\nMozzarella\n125\n50"