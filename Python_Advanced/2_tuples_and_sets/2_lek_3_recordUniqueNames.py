numbers_of_names=int(input())
all_names=set()
for x in range(numbers_of_names):
    name=input()
    all_names.add(name)

for m in all_names:
    print(m)
