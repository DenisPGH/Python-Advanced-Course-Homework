list_cards=input().split(", ")
n=int(input()) # 0-50

for one in range(n):
    command=input()
    command_info=command.split(", ")
    action=command_info[0]
    second_part=command_info[1]
    if action=="Add":   # "Add, {CardName}"
        if second_part not in list_cards:
            list_cards.append(second_part)
            print("Card successfully added")
        else:
            print("Card is already in the deck")
    elif action=="Remove":   #"Remove, {CardName}"
        if second_part in list_cards:
            list_cards.remove(second_part)
            print("Card successfully removed")
        else:
            print("Card not found")
    elif action=="Remove At":  # o	"Remove At, {index}"
        index_remove=int(second_part)
        if 0<=index_remove<len(list_cards):
            list_cards.pop(index_remove)
            print("Card successfully removed")
        else:
            print("Index out of range")
    elif action=="Insert":  #o	"Insert, {index}, {CardName}"
        index_insert = int(second_part)
        card_for_insert=command_info[2]
        if 0 <= index_insert < len(list_cards):
            if card_for_insert not in list_cards:
                list_cards.insert(index_insert,card_for_insert)
                print("Card successfully added")
            else:
                print("Card is already added")

        else:
            print("Index out of range")






# print all list on the end
print(", ".join(list_cards))