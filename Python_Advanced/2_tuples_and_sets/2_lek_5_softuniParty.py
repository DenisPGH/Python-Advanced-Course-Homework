number_of_quests=int(input())
all_guest_codes_set=set()
for a in range(number_of_quests):
    code=input()
    all_guest_codes_set.add(code)

while True:
    next_code=input()
    if next_code=="END":
        break
    all_guest_codes_set.remove(next_code)

print(len(all_guest_codes_set))
for a in sorted(all_guest_codes_set):
    print(a)








