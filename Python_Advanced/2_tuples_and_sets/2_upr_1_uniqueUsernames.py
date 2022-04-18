num_of_names=int(input())
all_unique_names=set()
for a in range(num_of_names):
    name=input()
    all_unique_names.add(name)

for m in all_unique_names:
    print(m)