from collections import deque

quantity_of_food=int(input())
order_line=deque([int(x) for x in input().split()])
print(max(order_line)) # print biggest order
#print(sum(order_line))
#print(order_line)
while quantity_of_food>0:

    if order_line :
        person = order_line[0]

        if person<=quantity_of_food:
            quantity_of_food-=person
            order_line.popleft()
        else:

            break
    else:
        break

#print(order_line)
if len(order_line)>0:
    print(f"Orders left: {' '.join([str(x) for x in order_line])}")
else:
    print("Orders complete")