from collections import deque

a_line={int(x) for x in input().split()}
b_line={int(x) for x in input().split()}
numbers=set()

numb_of_comands=int(input())
for a in range(numb_of_comands):
    comand_parts=deque(input().split())
    comand_type=comand_parts.popleft() # maha comand
    # •    "Add First {numbers, separated by a space}" - add
    # the
    # given
    # numbers
    # at
    # the
    # end
    # of
    # the
    # first
    # sequence
    # of
    # numbers.
    # •    "Add Second {numbers, separated by a space}" - add
    # the
    # given
    # numbers
    # at
    # the
    # end
    # of
    # the
    # second
    # sequence
    # of
    # numbers.

    if comand_type=="Add":
        which_sequence=comand_parts.popleft() # maha first/second

        numbers= {int(x) for x in comand_parts}
        if which_sequence=="First": # "Add First {numbers, separated by a space}"
            a_line=a_line.union(numbers)
        elif which_sequence=="Second": # "Add First {numbers, separated by a space}"
            b_line=b_line.union(numbers)

    # "Remove First {numbers, separated by a space}"
    if comand_type == "Remove":
        which_sequence = comand_parts.popleft()  # maha first/second

        numbers = [int(x) for x in comand_parts]
        if which_sequence == "First":  # "Add First {numbers, separated by a space}"
            a_line = a_line.difference(numbers)
        elif which_sequence == "Second":  # "Add First {numbers, separated by a space}"
            b_line = b_line.difference(numbers)
    # •	"Check Subset" - check if any of the given sequences are a subset of the other.
    # If it is, print "True". Otherwise, print "False".
    if comand_type == "Check":
       if a_line.issubset(b_line) or b_line.issubset(a_line):
           print(True)
       else:
           print(False)


# while a_line:
#     if len(a_line)>1:
#         print(a_line.pop(),end=", ")
#     else:
#         print(a_line.pop())
# while b_line:
#     if len(b_line)>1:
#         print(b_line.pop(),end=", ")
#     else:
#         print(b_line.pop())

print(*sorted(a_line), sep=", ")
print(*sorted(b_line), sep=", ")



