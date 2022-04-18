from my_fibonaccy_module.my_fibonacci_module import return_fibonaci as rf_list
current_sequence=[]
while True:
    command=input()
    if command=="Stop":
        break
    command_parts=command.split()
    action=command_parts[0]
    if action=="Create":  # •	"Create Sequence {count}".
        second_part = int(command_parts[2])
        current_sequence=rf_list(second_part)
        print(*rf_list(second_part))
    elif action=="Locate": # •	"Locate {number}"
        second_part = int(command_parts[1])
        if second_part in current_sequence:
            print(f"The number - {second_part} is at index {current_sequence.index(second_part)}")
        else:
            print(f"The number {second_part} is not in the sequence")


