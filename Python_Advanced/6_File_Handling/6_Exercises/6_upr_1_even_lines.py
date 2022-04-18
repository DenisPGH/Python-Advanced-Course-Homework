def create_directory_files(directory, contain): # def for creating a file
    with open(directory,"w") as searched_words:
        searched_words.write(contain)

text="""-I was quick to judge him, but it wasn't his fault.
-Is this some kind of joke?! Is it?
-Quick, hide here. It is safer.
"""
create_directory_files("text.txt",text)
signs=["-", ",", ".", "!", "?"]

try:
    with open("text.txt") as file:
        counter=0
        for each in file:  # for every line in the file
            sequence=each.split()[::-1]
            if counter %2==0:
                for word in range(len(sequence)): # for every word on current line
                    for letter in range(len(sequence[word])): # for every letter in current word
                        if sequence[word][letter].strip() in signs:
                            sequence[word]=sequence[word].replace(sequence[word][letter],"@")
                print(' '.join(sequence))
            counter+=1


except FileNotFoundError:
    print("File not found!")