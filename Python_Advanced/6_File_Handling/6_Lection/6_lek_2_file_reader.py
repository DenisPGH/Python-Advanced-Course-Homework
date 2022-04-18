with open("numbers") as file_numbers:
    result=0
    for a in file_numbers:
        result+=int(a.strip())
    print(result)