def sort_numbers(*args):
    positive_nums_sum=0
    negative_nums_sum=0
    result=""
    for n in range(len(args)):
        for num in args[n]:
            if num >0:
                positive_nums_sum+=num
            else:
                negative_nums_sum+=num

    result+=str(negative_nums_sum)+"\n"
    result+=str(positive_nums_sum)+"\n"
    if abs(negative_nums_sum)>positive_nums_sum:
        result+="The negatives are stronger than the positives"
    else:
        result+="The positives are stronger than the negatives"
    return result






numbers=[int(x) for x in input().split()]
print(sort_numbers(numbers))