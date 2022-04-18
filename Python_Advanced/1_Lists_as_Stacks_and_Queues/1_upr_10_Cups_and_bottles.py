from collections import deque
"""You could pick exactly one bottle at a time. If the current bottle has N water, 
you give the first entered cup N water and reduce its integer value by N.
When a cup's integer value reaches 0 or less, it gets removed. It is possible that the current
 cup's value is greater than the current bottle's value. In that case, you pick bottles until 
 you reduce the cup's integer value to 0 or less. If a bottle's value is greater or equal to the cup's 
 current value, you fill up the cup, and the remaining water becomes wasted.  """
cups_capacity= deque([int(x) for x in input().split()])
filled_bottles= [int(x) for x in input().split()]

waisted_watter=0

while filled_bottles and cups_capacity:
    current_bottle=filled_bottles.pop()
    current_cup=cups_capacity.popleft()
    if current_bottle>=current_cup:
        waisted_watter+=(current_bottle-current_cup)
    elif current_cup>current_bottle:
        current_cup-=current_bottle
        cups_capacity.appendleft(current_cup)

if not cups_capacity:
    print("Bottles:", end=" ")
    while filled_bottles:
        print(filled_bottles.pop(), end=" ")
else:
    print("Cups:", end=" ")
    while cups_capacity:
        print(cups_capacity.popleft(), end=" ")

print(f"\nWasted litters of water: {waisted_watter}")



