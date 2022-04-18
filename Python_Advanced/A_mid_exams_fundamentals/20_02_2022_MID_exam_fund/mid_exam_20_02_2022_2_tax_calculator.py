all_vehiles=input().split(">>")
allowed_types=["family","heavyDuty","sports"] # fam =50Ev  , heavy=80, sport=100ev
total_taxes=0
for each in all_vehiles:
    current_total_tax=0
    info_vehile=each.split()
    type=info_vehile[0]
    years_of_car=int(info_vehile[1])
    km_stand=int(info_vehile[2])
    # if type in allowed_types:
    if type=="family":
        current_total_tax=(50-(years_of_car*5))+((km_stand//3000)*12)
        total_taxes+=current_total_tax
    elif type=="heavyDuty":
        current_total_tax=(80-(years_of_car*8))+((km_stand//9000)*14)
        total_taxes += current_total_tax

    elif type=="sports":
        current_total_tax=(100-(years_of_car*9))+((km_stand//2000)*18)
        total_taxes += current_total_tax

    else:
        print("Invalid car type.")
        continue

    print(f"A {type} car will pay {current_total_tax:.2f} euros in taxes.")

print(f"The National Revenue Agency will collect {total_taxes:.2f} euros in taxes.")