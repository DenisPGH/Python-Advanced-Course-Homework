journal_items=input().split(", ")
while True:
    comand=input()
    if comand=="Craft!":
        break
    comand_info=comand.split(" - ")
    action=comand_info[0]
    item = comand_info[1]
    if action=="Collect": #	"Collect - {item}"
        if item not in journal_items:
            journal_items.append(item)
    elif action=="Drop": #•	"Drop - {item}"
        if item in journal_items:
            journal_items.remove(item)
    elif action== "Combine Items": #"Combine Items - {old_item}:{new_item}"
        old_item,new_item=item.split(":")
        if old_item in journal_items:
            journal_items.insert((journal_items.index(old_item)+1),new_item)
    elif action=="Renew" :  # •	"Renew – {item}"
        if item in journal_items:
            last_item=item
            journal_items.remove(item)
            journal_items.append(last_item)

print(", ".join(journal_items))

