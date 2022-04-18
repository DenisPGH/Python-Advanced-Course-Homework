stack_list=[int(x) for x in input().split()]
rack_capacity=int(input())
curren_capacity=rack_capacity
counter=1
while stack_list: # dokato ima drehi v stack lista
    dreha=stack_list[-1]

    if dreha<=curren_capacity:
        curren_capacity-=dreha
        stack_list.pop()
    else:
        curren_capacity=rack_capacity
        counter+=1

print(counter)
