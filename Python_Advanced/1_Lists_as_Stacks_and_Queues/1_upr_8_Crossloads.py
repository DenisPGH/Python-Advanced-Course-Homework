"""Input
•	On the first line, you will receive the duration of the green light in seconds – an integer [1 … 100]
•	On the second line, you will receive the duration of the free window in seconds – an integer [0 … 100]
•	On the following lines, until you receive the "END" command, you will receive one of two things:
	A car – a string containing the model of the car, or
	The command "green" that indicates the start of a green light cycle
"""
from collections import deque

duration_green_light=int(input())
duration_free_window=int(input())
green=False
success_passing_cars=0
all_cars=deque()
hitting=False
crashed_car=""
crashed_letter=''


while True:
    if hitting==True:
        break
    complet_time=duration_green_light+duration_free_window
    passing_string=input()
    if passing_string=="END":
        break
    if passing_string=='green':
        green=True
    if passing_string not in "ENDgreen":
        all_cars.append(passing_string)
    if green==True:
        while all_cars:
            if complet_time<= duration_free_window: # the car can go inside only in green
                break
            current_car=all_cars.popleft()

            if len(current_car)-complet_time >=1:
                hitting=True
                crashed_car=current_car
                crashed_letter=crashed_car[complet_time]
                break
            complet_time-=len(current_car)
            if complet_time < 0:
                all_cars.appendleft(current_car)
                green = False
                continue
            success_passing_cars += 1
        if len(all_cars)==0:
            green=False
            #continue




if not hitting:
    print("Everyone is safe.")
    print(f"{success_passing_cars} total cars passed the crossroads.")

else:
    print("A crash happened!")
    print(f"{crashed_car} was hit at {crashed_letter}.")



