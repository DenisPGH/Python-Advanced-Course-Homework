from collections import deque
toy_box_materials_stack=[int(x) for x in input().split()] # take last
magic_level=deque([int(x) for x in input().split()]) # take first
# Present	Magic needed
# Doll	            150
# Wooden train	250
# Teddy bear	300
# Bicycle 	        400
toys={150:{"name":"Doll","count":0},
      250: {"name":"Wooden train","count":0},
      300: {"name":"Teddy bear","count":0},
      400:  {"name":"Bicycle","count":0} }
success_christmas=False
while toy_box_materials_stack and magic_level:
    last_box_material=toy_box_materials_stack.pop()
    first_magic=magic_level.popleft()
    # case 3 •	If the magic or material (or both) equals 0,
    # remove it (or both) and continue crafting the presents.

    if last_box_material==0 and first_magic==0:
        continue
    if last_box_material==0:
        magic_level.appendleft(first_magic)
        continue
    if first_magic==0:
        toy_box_materials_stack.append(last_box_material)


    product= last_box_material * first_magic
    if product in toys:
        toys[product]["count"]+=1
    else:
        # case 1 •	If the product of the operation is a negative number, you should sum the values together,
        # remove them both from their positions, and add the result to the materials.
        if product <0:
            product= first_magic + last_box_material
            toy_box_materials_stack.append(product)
        # case 2 •	If the product doesn't equal one of the magic levels in the table
        # and is a positive number, remove only the magic value and increase the material value by 15.
        elif product > 0:
            toy_box_materials_stack.append(last_box_material + 15)

# Your task is considered done if you manage to craft either one of the pairs:
# •	a doll and a train
# •	a teddy bear and a bicycle
# toys={150:{"name":"Doll","count":0},
#       250: {"name":"Wooden train","count":0},
#       300: {"name":"Teddy bear","count":0},
#       400:  {"name":"Bicycle","count":0} }

if (toys[150]["count"]>0 and toys[250]["count"]>0) or (toys[300]["count"]>0 and toys[400]["count"]>0):
    success_christmas=True
# •	On the first line - print whether you've succeeded in crafting the presents:
# o	"The presents are crafted! Merry Christmas!"
# o	"No presents this Christmas!"
# •	On the next two lines print the materials and magic that are left,
# if there are any (otherwise skip the line)

# o	"Materials left: {material_N}, {material_N-1}, … {material_1}"
# o	"Magic left: {magicValue_1}, {magicValue_2}, … {magicValue_N}"
#
# print(toy_box_materials_stack)
# print(magic_level)
# print(sorted(magic_level,reverse=True))
# print(sorted(toy_box_materials_stack,reverse=True))
 #print(f"Materials left: {', '.join([str(x) for x in sorted(toy_box_materials_stack,reverse=True)])}")

if success_christmas:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if toy_box_materials_stack:
    print("Materials left:", end=" ")
    while toy_box_materials_stack:
        if len(toy_box_materials_stack)>1:
            print(toy_box_materials_stack.pop(),end=", ")
        else:
            print(toy_box_materials_stack.pop())


if magic_level:
    print("Magic left:", end=" ")
    while magic_level:
        if len(magic_level)>1:
            print(magic_level.popleft(),end=", ")
        else:
            print(magic_level.popleft())

#•	On the next lines print the presents you have crafted, ordered alphabetically in the format:
# o	"{toy_name1}: {amount}
# {toy_name2}: {amount}
# ...
# {toy_nameN}: {amount}"

for key, value in sorted(toys.items(),key= lambda x: (-x[1]['count']>0,x[1]["name"])):
    if value['count']>0:
        print(f"{value['name']}: {value['count']}")





