import math

george_budget=float(input())
students=int(input())
price_package_floor=float(input())
price_single_egg=float(input())
price_package_arpon=float(input())
# set one students = 1 packet floor, 10 eggs, an arpon   20% more arpons, every 5th floor is free

one_students_package= price_package_floor+(10*price_single_egg)+price_package_arpon
sum_costs=0
for each in range(1,students+1):
    sum_costs+=price_package_floor # add floor
    sum_costs+=10*price_single_egg # add egs
    sum_costs+=price_package_arpon # add arpon
    if each %5==0:
        sum_costs-=price_package_floor
sum_costs+= math.ceil(students*0.2)*price_package_arpon

if sum_costs<=george_budget: # succes
    print(f"Items purchased for {sum_costs:.2f}$.")
else:
    print(f"{sum_costs-george_budget:.2f}$ more needed.")

