from collections import deque
kids=deque(input().split())


step=int(input())

while len(kids)>1:
    kids.rotate(-step)
    print(f"Removed {kids[-1]}")
    #print(f"Removed {kids.pop()}")
    kids.pop()



print(f"Last is {kids.pop()}")