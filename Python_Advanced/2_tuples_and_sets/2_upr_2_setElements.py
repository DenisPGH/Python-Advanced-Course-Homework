n,m=input().split()
set_n=set()
set_m=set()
for _ in range(int(n)):
    numb_n=int(input())
    set_n.add(numb_n)
for _ in range(int(m)):
    numb_m = int(input())
    set_m.add(numb_m)


for a in (set_n.intersection(set_m)):
    print(a)