from collections import deque

bomb_effects=deque([int(x) for x in input().split(", ")])
bomb_casings=[int(x) for x in input().split(", ")]
bombs_dict={ 40 : "Datura Bombs",
             60 : "Cherry Bombs",
             120 : "Smoke Decoy Bombs"
             }
created_bombs={"Datura Bombs": {"value" : 0},
              "Cherry Bombs": {"value" : 0},
             "Smoke Decoy Bombs": {"value" : 0}
               }
success=False
while bomb_casings and bomb_effects:
    curent_bomb_efect=bomb_effects.popleft()
    current_casing= bomb_casings.pop()
    result=curent_bomb_efect+current_casing
    if result in bombs_dict:
        created_bombs[bombs_dict[result]]["value"] += 1
        # if created_bombs[bombs_dict[result]]["value"]<3:


    else:
        current_casing-=5
        bomb_casings.append(current_casing)
        bomb_effects.appendleft(curent_bomb_efect)
    all_=all([True if x['value']>=3 else False for x in created_bombs.values()])
    if all_ :
        success=True
        break


if success:
    print(f"Bene! You have successfully filled the bomb pouch!")
if not success:
    print(f"You don't have enough materials to fill the bomb pouch.")
if not bomb_effects:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")
if not bomb_casings:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casings])}")

print(f"Cherry Bombs: {created_bombs['Cherry Bombs']['value']}\n"
      f"Datura Bombs: {created_bombs['Datura Bombs']['value']}\n"
      f"Smoke Decoy Bombs: {created_bombs['Smoke Decoy Bombs']['value']}")




