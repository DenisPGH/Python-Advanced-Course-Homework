numbers_dictionary = {}

line = input()

while line != "Search": # •	On the first several lines, until you receive the command "Search",
                            # you will receive on separate lines the number as a text and the number as an integer
    number_as_string = line
    number = input()
    if number.isdigit():
        number = int(number)
        numbers_dictionary[number_as_string] = number
    else:
        print("The variable number must be an integer")


    line=input()




#•	When you receive "Search" on the next several lines until you receive the command "Remove",
# you will be given the searched number as a text, and you need to print it on the console
line_ = input()
while line_ != "Remove":
    searched = line_
    if searched in numbers_dictionary:
        print(numbers_dictionary[searched])
    else:
        print("Number does not exist in dictionary" )
    line_=input()





#•	When you receive "Remove" on the next several lines until you receive "End",
# you will be given the searched number as a text, and you need to remove it from the dictionary
line_e = input()
while line_e != "End":
    searched = line_e
    if searched in numbers_dictionary:
        del numbers_dictionary[searched]
    else:
        print("Number does not exist in dictionary" )
    line_e=input()


#•	In the end, you need to print what is left from the dictionary
print(numbers_dictionary)
