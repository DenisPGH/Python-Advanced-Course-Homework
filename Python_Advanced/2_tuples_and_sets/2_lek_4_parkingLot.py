numbers_of_cars=int(input())
all_cars=set()
for n in range(numbers_of_cars):
    direction, car=input().split(", ")
    if direction== "IN":
        all_cars.add(car)
    elif direction== "OUT":
        all_cars.remove(car)

if all_cars:
    for car in all_cars:
        print(car)
else:
    print("Parking Lot is Empty")