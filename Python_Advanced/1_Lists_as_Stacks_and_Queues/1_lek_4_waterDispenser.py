from collections import deque
start=False
line_people=deque()
quantity_water=int(input())
while True:
    text=input()
    if text== "End":
        break
    if text=="Start":
        start=True
        continue
    if not start: # store the peope
        line_people.append(text)

    if start: # start trinking

        if text.isdigit(): # first person want to trink
            if int(text)<=quantity_water:
                quantity_water-=int(text)
                print(f"{line_people[0]} got water" )
            else: # less water
                print(f"{line_people[0]} must wait" )
            line_people.popleft()


        else:  # that comand fill with water -	"refill {liters}" - add
            text_info=text.split()
            water_value=text_info[1]
            quantity_water+=int(water_value)

print(f"{quantity_water} liters left")


