def age_assignment(*args,**kwargs):
    persons={}
    for a in args:
        persons[a]=0
        for k,v in kwargs.items():
            if a[0]==k:
                persons[a]=v


    return persons



#print(age_assignment("Peter", "George", G=26, P=19))	# {'Peter': 19, 'George': 26}
#print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61)) # 	{'Amy': 22, 'Bill': 61, 'Willy': 36}
