
def start_spring (**kwargs):
    flower=set([x for x in kwargs.values()])
    end_dict={}
    for k,v in kwargs.items():
        if v not in end_dict:
            end_dict[v]=[]
        end_dict[v].append(k)


    result=''
    for type_,list_ in sorted(end_dict.items(),key= lambda x:(-(len(x[1])),x[0])):
        result+=f"{type_}:"+'\n'
        for each in sorted(list_):
            result+=f"-{each}"+'\n'
    return result

# example_objects = {"Water Lilly": "flower",
#                    "Swifts": "bird",
#                    "Callery Pear": "tree",
#                    "Swallows": "bird",
#                    "Dahlia": "flower",
#                    "Tulip": "flower",}
# print(start_spring(**example_objects))
#
#
# example_objects = {"Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Woodpeckers": "bird",
#                    "Swallows": "bird",
#                    "Warblers": "bird",
#                    "Shrikes": "bird",}
# print(start_spring(**example_objects))
#
# example_objects = {"Magnolia": "tree",
#                    "Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Pear": "tree",
#                    "Cherries": "tree",
#                    "Shrikes": "bird",
#                    "Butterfly": "insect"}
# print(start_spring(**example_objects))
#
