number_of_lines=int(input())
even_set=set()
odd_set=set()
even_sum=0
odd_sum=0

for counter in range(1,number_of_lines+1):
    sum_ascii_of_name=0
    name=input().strip()
    for char in name:
        sum_ascii_of_name+=ord(char)
    result=sum_ascii_of_name//counter

    if result%2==0 : # even row
        even_set.add(result)
        even_sum+=result
    elif result %2 !=0:
        odd_set.add(result)
        odd_sum+=result

# even_sum=sum(even_set)
# odd_sum=sum(odd_set)
if even_sum==odd_sum: # if equal print union
    print(', '.join({str(x) for x in odd_set.union(even_set)}))
elif odd_sum > even_sum:
    print(', '.join({str(x) for x in odd_set.difference(even_set)}))
elif odd_sum < even_sum:
    print(', '.join({str(x) for x in odd_set.symmetric_difference(even_set)}))
