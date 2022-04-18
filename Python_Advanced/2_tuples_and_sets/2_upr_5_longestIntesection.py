
number_of_lines=int(input())
max_intesetction=-200
max_numbers=set()
for a in range(number_of_lines):
    team_a=set()
    team_b=set()
    sequence= input().split("-")  # "{first_start},{first_end}-{second_start},{second_end}".
    a_start,a_end=sequence[0].split(",")
    b_start,b_end=sequence[1].split(",")
    for a in range(int(a_start),int(a_end)+1):
        team_a.add(a)
    for b in range(int(b_start),int(b_end)+1):
        team_b.add(b)
    #print(len(team_a.intersection(team_b)))
    if len(team_a.intersection(team_b))> max_intesetction:
        max_intesetction=len(team_a.intersection(team_b))
        max_numbers=team_a.intersection(team_b)



list_numbers=[]
for a in max_numbers:
    list_numbers.append(a)


print(f"Longest intersection is [{', '.join([str(x) for x in sorted(list_numbers)])}] with length {max_intesetction}")