text=input()
dict_chars={}

for char in text:
    if char not in dict_chars:
        dict_chars[char]=0
    dict_chars[char]+=1


for key,v in sorted(dict_chars.items()):
    print(f"{key}: {v} time/s")
