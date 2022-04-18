status_of_pirate_ship= [int(x) for x in input().split(">")]
status_of_warship= [int(x) for x in input().split(">")]
maximum_health_capacity =int(input())
break_loop=False
while True:
    comand=input()
    if comand== "Retire":
        break
    comand_parts=comand.split()
    action=comand_parts[0]
    if action=="Fire": #	"Fire {index} {damage}"
        fire_index=int(comand_parts[1])
        fire_damage=int(comand_parts[2])
        if 0<=fire_index<len(status_of_warship): # check if index is valid
            status_of_warship[fire_index]-=fire_damage # reduce the value
            if status_of_warship[fire_index]<=0: # if less zero break
                print("You won! The enemy ship has sunken.")
                break_loop=True
                break

    elif action =="Defend":  # 	"Defend {startIndex} {endIndex} {damage}"
        defend_start_index=int(comand_parts[1])
        defend_end_index=int(comand_parts[2])
        defend_damage=int(comand_parts[3])
        if 0<=defend_start_index<len(status_of_pirate_ship) and 0<=defend_end_index<len(status_of_pirate_ship):
            for each_ship in range(defend_start_index,defend_end_index+1):
                status_of_pirate_ship[each_ship]-=defend_damage
                if status_of_pirate_ship[each_ship]<=0:
                    print(f"You lost! The pirate ship has sunken.")
                    break_loop=True
                    break

    elif action=="Repair": # •	"Repair {index} {health}"
        repair_index=int(comand_parts[1])
        repair_health=int(comand_parts[2])
        if 0<= repair_index <len(status_of_pirate_ship): # if the index is valid
            status_of_pirate_ship[repair_index]+=repair_health
            if status_of_pirate_ship[repair_index]>maximum_health_capacity:
                status_of_pirate_ship[repair_index]=maximum_health_capacity


    elif action== "Status":  # •	"Status"
        count=0
        for each in range(len(status_of_pirate_ship)):
            if status_of_pirate_ship[each]< maximum_health_capacity*0.2:
                count+=1

        print(f"{count} sections need repair.")



    if break_loop:
        break

    #print(status_of_warship)
    #print(status_of_pirate_ship)


if not break_loop:
    print(f"Pirate ship status: {sum(status_of_pirate_ship)}")
    print(f"Warship status: {sum(status_of_warship)}")

# list_a=[1,2,3,4,5,6]
# for e in range(2,3+1):
#     print(list_a[e])