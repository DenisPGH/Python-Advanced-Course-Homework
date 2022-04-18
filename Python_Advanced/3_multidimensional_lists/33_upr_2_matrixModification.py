def valid_coord(row:int,cow:int,complet_colums:list):
    if 0<=row<numb_rows and 0<=cow<len(complet_colums):
        return True

def valid_rows(row:int):
    if 0<= row<numb_rows:
        return True

numb_rows=int(input())
matrix=[]
for r in range(numb_rows):
    matrix.append([int(x) for x in input().split()])
while True:
    comand_input=input()
    if comand_input== "END":
        break
    comand,row, cow, value= comand_input.split()
    row=int(row)
    cow=int(cow)
    value=int(value)
    if not valid_rows(row):
        print("Invalid coordinates")
        continue

    if valid_coord(row,cow,matrix[row]):
        if comand== "Subtract":
            matrix[row][cow]-=value
        elif comand== "Add":
            matrix[row][cow]+=value
        else:
            pass
    else:
        print("Invalid coordinates")



for a in range(numb_rows):
    print(*matrix[a],sep=" ")
