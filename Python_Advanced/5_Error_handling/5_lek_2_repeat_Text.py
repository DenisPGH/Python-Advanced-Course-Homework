
while True:
    try:
        text=input()
        # add from me
        if text== "end":
            print("END!")
            break
        count=int(input())
        print(text*count)


    except ValueError:
        print("Variable times must be an integer")
        text = input()
        count=int(input())
        print(text * count)