from collections import deque
def return_new_word(word:str): # without last letter
    new_word=deque(word)
    if len(new_word)>1:
        new_word.pop()
        return ''.join(new_word)
    # else:
    #     new_word=""
    #     return None




text=deque([x for x in input().split()])
main_colours=["red", "yellow", "blue"]
secondary_colours=["orange", "purple", "green"]
#print(text)
words_for_print=[]
second_word=[]

while text:
    first=text.popleft()
    if text:
        last=text.pop()
    else:
        last=""



    #print(combine_word)
    if first+last in main_colours or first+last in secondary_colours: # find maches
        words_for_print.append(first+last)
    elif last + first in main_colours or last + first in secondary_colours:  # find maches
        words_for_print.append(last + first)


    # if first+last in secondary_colours:
    #     words_for_print.append(first+last)  # ako ima drugi cvetove
    # elif last + first in secondary_colours:
    #     words_for_print.append(last + first)  # ako ima drugi cvetove

    else:  # no mathes
        middle_index = len(text) // 2
        first = return_new_word(first)
        last = return_new_word(last)
        if first != None:
            text.insert(middle_index, first)
        if last != None:
            text.insert(middle_index, last)




#print(words_for_print)
#print(second_word)
requered= {
    'orange': ['red', 'yellow'],
    'purple' : ['red', 'blue'],
    'green' : ['yellow', 'blue'],
}
last=[]
for each in words_for_print:
    if each in main_colours:
        last.append(each)
    else:
        nope = True
        for a in requered[each]:
            if a not in words_for_print:
                nope=False
        if nope:
            last.append(each)



print(last)

