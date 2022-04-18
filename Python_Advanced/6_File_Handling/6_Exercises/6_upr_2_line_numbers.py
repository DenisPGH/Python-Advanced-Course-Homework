try:
    with open("text.txt") as file:
        counter=1

        for each in file:  # for every line in the file
            sequence=each.split()
            counter_leters = 0
            counter_marks = 0
            for word in range(len(sequence)): # for every word on current line
                for letter in range(len(sequence[word])): # for every letter in current word
                    if sequence[word][letter].isalpha():
                        counter_leters+=1
                    else:
                        counter_marks+=1

            with open("output.txt", "a") as file_output: # write the result to other file named output
                file_output.write(f"Line {counter}: {' '.join(sequence)} ({counter_leters})({counter_marks})\n")
               # print(f"Line {counter}: {' '.join(sequence)} ({counter_leters})({counter_marks})")
            counter+=1


except FileNotFoundError:
    print("File not found!")