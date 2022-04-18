# "{10_upr_4_student's name} -> {grade1} {grade2} ... {gradeN} (avg: {average_grade})".
num_students= int(input())
students_dict={}
for a in range(num_students):
    student=input()
    name, note=student.split()
    if name not in students_dict:
        students_dict[name]=[]
    students_dict[name].append(float(note))
for k,v in students_dict.items():
    print(f"{k} -> {' '.join([f'{x:.2f}' for x in v])} (avg: {sum(v)/len(v):.2f})")

