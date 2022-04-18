from collections import deque
line_people=deque()
while True:
    text=input()
    if text== "End" :
        break

    if text=="Paid":
        while line_people:
            print(line_people.popleft())
    else:
        line_people.append(text)

print(f"{len(line_people)} people remaining.")
