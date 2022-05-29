from collections import deque

def check_if_all_letters(all:list,dict_:dict):
    found=False
    word_end=""
    for word in all:
        list_word=list(word)
        list_word_copy=set(deque(list_word.copy()))
        letters_copy=dict_[word].copy()
        words_left=[]
        if letters_copy:
            while list_word_copy :
                first_letter=list_word_copy.pop()
                if first_letter in letters_copy:
                    letters_copy.remove(first_letter)
                else:
                    words_left.append(first_letter)


            #if not words_left and not letters_copy:
            if not words_left:
                found= True
                word_end=word
                break
            else:
                found=False

    return word_end








vowels_collection=deque(input().split())
consonants_collection=input().split()
all_flowers=["rose", "tulip", "lotus", "daffodil"]
#all_flowers=["daffodil"]
found_letters={}
found_word=''
found=False
for each in all_flowers:
    found_letters[each] = []
while vowels_collection and consonants_collection:
    first_vowels=vowels_collection.popleft()
    last_consonants=consonants_collection.pop()
    for each in all_flowers:
        if first_vowels in each:
            found_letters[each].append(first_vowels)
        if last_consonants in each:
            found_letters[each].append(last_consonants)
    if check_if_all_letters(all_flowers,found_letters) !="":
        found_word=check_if_all_letters(all_flowers,found_letters)
        found=True
        #print(found_letters)
    if found:
        break



if found_word !='':
    print(f"Word found: {found_word}")
else:
    print("Cannot find any word!")

if vowels_collection:
    print(f"Vowels left: {' '.join(vowels_collection)}")

if consonants_collection:
    print(f"Consonants left: {' '.join(consonants_collection)}")


#print(found_letters)

