initial_treasure_chest =input().split("|")
while True:
    comand=input()
    if comand== "Yohoho!":
        break
    comand_parts=comand.split()
    action=comand_parts[0]
    new_treasure=comand_parts[1:]
    #print(new_treasure)
    # •    "Loot {item1} {item2}…{itemn}":
    # o
    # Pick
    # up
    # treasure
    # loot
    # along
    # the
    # way.Insert
    # the
    # items
    # at
    # the
    # beginning
    # of
    # the
    # chest.
    # o
    # If
    # an
    # item is already
    # contained, don
    # 't insert it.

    if action=="Loot": #	"Loot {item1} {item2}…{itemn}":
        for each in new_treasure:
            if each not in initial_treasure_chest:
                initial_treasure_chest.insert(0,each)

    if action =="Drop": #	"Drop {index}":
        index=int(comand_parts[1])
        if index<0 or index>(len(initial_treasure_chest)-1):
            continue
        for_move=initial_treasure_chest[index]
        initial_treasure_chest.pop(index)
        initial_treasure_chest.append(for_move)
    if action == "Steal":  # •	"Steal {count}":
        count = int(comand_parts[1])
        try:
            stealed_loot=initial_treasure_chest[-count:]
            del initial_treasure_chest[-count:]
        except IndexError:
            stealed_loot = initial_treasure_chest
            del initial_treasure_chest

        print(', '.join(stealed_loot))




    #print(initial_treasure_chest)


if initial_treasure_chest:
    sum_=0
    for a in initial_treasure_chest:
        sum_+=len(a)

    average=sum_/len(initial_treasure_chest)
    print(f"Average treasure gain: {average:.2f} pirate credits.")
else:
    print(f"Failed treasure hunt.")