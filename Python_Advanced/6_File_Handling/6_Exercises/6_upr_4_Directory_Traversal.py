import os
import re
pattern= r"\.[a-z]+"
type_folders={} # here store all types

for each in os.listdir("example"): # for every file name in example folder
    type=re.findall(pattern,each) # using regex to find the type of the file
    type=''.join(type)
    #print(type)
    if type not in type_folders: # store in the dictionaries
        type_folders[type]=[]
    type_folders[type].append(each)

# # printing the result sorted
# for type,files in sorted(type_folders.items(), key= lambda x: x[0]):
#     print(type)
#     for each_file in sorted(files):
#         print(f"- - - {each_file}")

# store the result in file report
with open("report.txt", "a") as report:
    for type, files in sorted(type_folders.items(), key=lambda x: x[0]):
        report.write(f"{type}\n")
        for each_file in sorted(files):
            report.write(f"- - - {each_file}\n")
