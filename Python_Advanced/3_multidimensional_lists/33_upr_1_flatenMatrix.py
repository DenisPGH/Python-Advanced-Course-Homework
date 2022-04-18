from collections import deque
# 1 2 3 |4 5 6 |  7  88
xx=[" ","  ","   ","    ","     ","       ","        ",'      ']

text= deque([' '.join([str(y.strip()) for y in x.split()]) for x in input().split('|') if x not in xx])
#print(' '.join(reversed(text)))
while text:
    print(text.pop(),end=' ')
