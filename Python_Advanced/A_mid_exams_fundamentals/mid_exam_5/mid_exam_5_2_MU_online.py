# initial health 100 and initial bitcoins 0.
all_rooms= input().split('|')
my_initial_health=100
my_initial_bitcoins=0
dead=False
for each in all_rooms:
    info_room=each.split()
    command=info_room[0]
    number=int(info_room[1])
    if command == "potion":
        getted_value=0
        if my_initial_health+number>100:
            getted_value=number-((my_initial_health+number)-100)
        else:
            getted_value=number
        my_initial_health+=getted_value
        print(f"You healed for {getted_value} hp.")
        print(f"Current health: {my_initial_health} hp.")
    elif command=="chest":
        my_initial_bitcoins+=number
        print(f"You found {number} bitcoins.")
    else: # meet a monster
        my_initial_health-=number # it reduce my power
        if my_initial_health>0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {(all_rooms.index(each)+1)}")
            dead=True
            break

if not dead:
    print("You've made it!")
    print(f"Bitcoins: {my_initial_bitcoins}")
    print(f"Health: {my_initial_health}")
