import re

def create_directory_files(directory, contain): # def for creating a file
    with open(directory,"w") as searched_words:
        searched_words.write(contain)

def return_searching_words(directory): # return a list with words in the text.filed
    try:
        with open(directory) as file:
            result = file.read().split()
            return result
    except FileNotFoundError:
        print("The directory not found!")

def return_input(directory):  # this function return the input_text
    try:
        with open(directory) as file:
            return file.read()
    except FileNotFoundError:
        print("The directory not found!")

matches_word={}
text_input="""-I was quick to judge him, but it wasn't his fault.
-Is this some kind of joke?! Is it?
-Quick, hide here…It is safer.
"""
create_directory_files("words.txt", "quick is fault") # create the file with the searched words
create_directory_files("input.txt", text_input) # create the file with the input

# here story all date in the dictionary
for each in return_searching_words("words.txt"):
    counter=re.findall(fr"\b{each}\b",return_input("input.txt"),re.IGNORECASE)
    if each not in matches_word:
        matches_word[each]=len(counter)

#print the sorted result in the dictionaries
for word,count in sorted(matches_word.items(),key= lambda x: -x[1]):
    print(f"{word}-{count}")

# print(return_input("deni.txt")) probe if the code works with wrong directory