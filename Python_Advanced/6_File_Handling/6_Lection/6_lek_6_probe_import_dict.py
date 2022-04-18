import json

try:
    with open("probe_dict_date") as file:
        working_dict= json.load(file)
        # for k in working_dict:
        #     print(f"{k}=={working_dict[k]}")
        for k in sorted(working_dict,key= lambda x: x[0],reverse=True):
            print(f"{k}=={working_dict[k]}")



except FileNotFoundError:
    print("The dictionary is not found!")
