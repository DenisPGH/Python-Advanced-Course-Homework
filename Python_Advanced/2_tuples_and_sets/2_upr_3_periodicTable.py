number_of_rows=int(input())
all_signs=set()
for _ in range(number_of_rows):
    line=input().split()
    for l in line:
        all_signs.add(l)

for s in (all_signs):
    print(s)