# 2 3
# 1 2 3
# 4 5 6
row,col=[int(x) for x in input().split()]
matrix=[]
for r in range(row):
    matrix.append([x for x in input().split()])
#print(matrix)

while True:
    comand=input()
    if comand=="END":
        break
    # "swap {row1} {col1} {row2} {col2}"
    parts_of_comand=comand.split()
    if len(parts_of_comand)== 5 and parts_of_comand[0] == "swap":
        r1=int(parts_of_comand[1])
        c1=int(parts_of_comand[2])
        r2=int(parts_of_comand[3])
        c2=int(parts_of_comand[4])
        if (0<= r1 < row) and( 0<= c1 <col) and (0<= r2 < row ) and (0<= c2 <col):
            matrix[r1][c1],matrix[r2][c2]=matrix[r2][c2],matrix[r1][c1]
            for a in matrix:
                print(' '.join([str(y) for y in a]))

        else:
            print("Invalid input!")

    else :
        print("Invalid input!")
