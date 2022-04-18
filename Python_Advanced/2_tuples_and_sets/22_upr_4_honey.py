from collections import deque
working_bees=deque([int(x) for x in input().split()])
nectar_skack=[int(x) for x in input().split()]
symbols=deque(x for x in input().split())
honey=0
while nectar_skack and working_bees:
    first_bee=working_bees.popleft()
    last_nectar=nectar_skack.pop()

    if last_nectar>=first_bee and last_nectar>0: # collected honey
        first_symbol = symbols.popleft()
        if first_symbol=="+":
            honey+=abs(first_bee+last_nectar)
        elif first_symbol=="-":
            honey+=abs(first_bee-last_nectar)
        elif first_symbol=="*":
            honey += abs(first_bee * last_nectar)
        elif first_symbol=="/":
            honey += abs(first_bee / last_nectar)

    elif last_nectar<first_bee: # less necktar
        working_bees.appendleft(first_bee) # return the bee, only remove the nectar


print(f"Total honey made: {honey}")
if working_bees:
    print(f"Bees left: {', '.join([str(x) for x in working_bees])}")
if nectar_skack:
    print(f"Nectar left: {', '.join([str(x) for x in nectar_skack])}")



