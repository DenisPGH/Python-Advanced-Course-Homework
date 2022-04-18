try:
    with open("text") as file:
        print('File found>>>>>>>>\n')
        print(file.read())
except FileNotFoundError:
    print('File not found')