from collections import deque
chocolates_stack=[int(x) for x in input().split(", ")] # from last
cups_milk=deque([int(x) for x in input().split(", ")]) # from first
milkshakes_counter=0
success=False

while chocolates_stack and cups_milk:

    choco = chocolates_stack.pop()
    cup = cups_milk.popleft()
    if choco<=0 and cup<=0:
        continue

    if cup<=0:
        chocolates_stack.append(choco)
        continue
    if choco<=0:
        cups_milk.appendleft(cup)
        continue


    if  choco== cup : # if both same , remove both == milkshakes
        milkshakes_counter+=1
    else:
        cups_milk.append(cup)
        chocolates_stack.append(choco-5)
    if milkshakes_counter >=5:
        success=True
        break



if success:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print(f"Not enough milkshakes.")
if chocolates_stack:
    print(f"Chocolate: {', '.join([str(x) for x in chocolates_stack])}")
else:
    print(f"Chocolate: empty")
if cups_milk:
    print(f"Milk: {', '.join([str(x) for x in cups_milk])}")
else:
    print("Milk: empty")