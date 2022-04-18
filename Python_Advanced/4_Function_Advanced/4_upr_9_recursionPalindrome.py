def palindrome(word,zero):
    midd=len(word)//2
    first_part=word[:midd+1]
    second_part=word[midd:][::-1]
    if zero==midd:
        return f'{word} is a palindrome'
    if first_part[zero]==second_part[zero]:
        return palindrome(word,zero+1)
    else:
        return f"{word} is not a palindrome"






# print(palindrome("abcba", 0))	# abcba is a palindrome
# print(palindrome("peter", 0)) # 	peter is not a palindrome
