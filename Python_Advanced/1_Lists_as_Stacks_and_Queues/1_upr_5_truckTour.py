from collections import deque

num_of_gas=int(input())
all_gas_stattions=deque()
for _ in range(num_of_gas):
    all_gas_stattions.append([int(x) for x in input().split()])
#print(all_gas_stattions)

actual_gas=0
counter_durch_gas=0
for b in range(len(all_gas_stattions)): # try times=gas
    counter_durch_gas = 0
    actual_gas=0
    for a in range(len(all_gas_stattions)): # try with each das station
        quantity=all_gas_stattions[a][0]
        actual_gas+=quantity
        distance=all_gas_stattions[a][1]
        if actual_gas>= distance: # if I have enought gas till next station
            actual_gas-=distance
            counter_durch_gas+=1
        else:
            break
    if counter_durch_gas == len(all_gas_stattions):  # if all gas gone trought stop

        print(b)
        break
    else:
        all_gas_stattions.rotate(-1)



    # for amount, distance in all_gas_stattions:
    #     print(f"{amount},{distance}")


