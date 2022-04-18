import math

number_students=int(input())
number_lectrure=int(input())
bonus_additional=int(input())
max_bonus=0
max_attendance=0
current_bonus_sum=0


for st in range(number_students): # {total bonus} = {10_upr_4_student attendances} / {course lectures} * (5 + {additional bonus}
    attendance = input()
    if attendance and attendance !=" ":
        current_bonus_sum = (int(attendance) / number_lectrure) * (5 + bonus_additional)
        if current_bonus_sum > max_bonus:
            max_bonus = current_bonus_sum
            max_attendance = int(attendance)
        #attendance = input()


print(f"Max Bonus: {math.ceil(max_bonus)}.")
print(f"The student has attended {max_attendance} lectures.")