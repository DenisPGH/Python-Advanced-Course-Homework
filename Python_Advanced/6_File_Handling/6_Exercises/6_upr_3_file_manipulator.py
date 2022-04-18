import os


def create_file(name):
    # •	"Create-{file_name}" - Creates the given file with an empty content.
    # If the file already exists, remove the existing text in it (as if the file is created again)
        with open(name,"w") as name_file:
            name_file.write("")


def add_file_content(file, content):
    # •	"Add-{file_name}-{content}" - Append the content and a new line after it.
    # If the file does not exist, create it, and add the content
    with open(file, "a") as name_file:
        name_file.write(f"{content}\n")


def repalce_text(name,old_string, new_string):
    # •	"Replace-{file_name}-{old_string}-{new_string}" - Open the file and replace
    # all the occurrences of the old string with the new string. If the file does not exist,
    # print: "An error occurred"
    try:
        with open(name) as name_file:
            text= name_file.read()
            if old_string in text:
                text=text.replace(old_string,new_string)
                with open(name, 'w') as file:
                    file.write(text)
            else:
                print("An error occurred(by replace)")


    except FileNotFoundError:
        print("An error occurred(by replace)")


def delete_file(name):
    # •	"Delete-{file_name}" - Delete the file. If the file does not exist, print: "An error occurred"
    try:
        if os.path.exists(name):
            os.remove(name)
        else:
            print("An error occurred(by deleting)")
    except FileNotFoundError:
        print("An error occurred(by deleting)")



while True:
    command=input()
    if command=="End":
        break
    command_parts=command.split("-")
    action=command_parts[0]
    file_name = command_parts[1]

    if action== "Create":
        create_file(file_name)

    elif action== "Add":
        file_content=command_parts[2]
        add_file_content(file_name,file_content)


    elif action== "Replace": # "Replace-{file_name}-{old_string}-{new_string}"
        old_string=command_parts[2]
        new_string=command_parts[3]
        repalce_text(file_name,old_string,new_string)


    elif action== "Delete":
        delete_file(file_name)