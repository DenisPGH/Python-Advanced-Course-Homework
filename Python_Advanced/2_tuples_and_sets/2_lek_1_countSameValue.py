# -2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3
# print "{number} - {count} times".
numbers=[float(x) for x in input().split()]
dict_num_counter={}
for n in numbers:
    if n not in dict_num_counter:
        dict_num_counter[n]=0
    dict_num_counter[n]+=1

#print(dict_num_counter)
for k,v in dict_num_counter.items():
    print(f"{k:.1f} - {v} times")