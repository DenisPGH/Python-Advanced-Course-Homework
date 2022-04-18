from collections import deque

pizza_orders=deque([int(x) for x in input().split(', ')])
employees=[int(x) for x in input().split(", ")]
total_pizas=0
while pizza_orders and employees:
    current_pizza_order=pizza_orders.popleft()
    if current_pizza_order<=0 or current_pizza_order>10:
        continue
    last_employee=employees.pop()
    if current_pizza_order<=last_employee:
        total_pizas+=current_pizza_order

    elif  current_pizza_order>last_employee:
        current_pizza_order-=last_employee
        pizza_orders.appendleft(current_pizza_order)
        # if no more employes, consider not complete



if not pizza_orders:
    print(f"All orders are successfully completed!\n"
          f"Total pizzas made: {total_pizas}\n"
          f"Employees: {', '.join([str(x) for x in employees])}")
else:
    print(f"Not all orders are completed.\n"
          f"Orders left: {', '.join([str(x) for x in pizza_orders])}")


"""
10, 9, 8, 7, 5
5, 10, 9, 8, 7
"""