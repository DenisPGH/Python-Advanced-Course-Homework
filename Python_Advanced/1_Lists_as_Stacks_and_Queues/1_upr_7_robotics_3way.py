from collections import deque
products=deque()

def get_sec_from_TIME(time_str:str,add_sec:int): # 8:00:00 # 28 801
    """Get Seconds from time."""
    h, m, s = time_str.split(':')
    seconds=(int(h) * 3600 + int(m) * 60 + (int(s)))  # 86399 end day 23.59.59
    #print(seconds)

    if seconds+add_sec > 86400:
        seconds=add_sec-1
    else:
        seconds+=add_sec

    # CONVERT BACK TO STRING
    #print(seconds)
    hh = seconds // (60 * 60)
    mm = (seconds - hh * 60 * 60) // 60
    ss = seconds - (hh * 60 * 60) - (mm * 60)
    if hh==24:
        hh=0
    return f"{hh:02d}:{mm:02d}:{ss:02d}"


def only_sec(time_str:str): # 8:00:00 # 28 801
    """Get Seconds from time."""
    h, m, s = time_str.split(':')
    seconds=(int(h) * 3600 + int(m) * 60 + (int(s)))  # 86399 end day 23.59.59
    return seconds



robots=[str(x) for x in input().split(";")] # get the robots from input
dict_robots={}

work="work"
status="status"
for a in robots: # store all robots in the dict
    b=a.split("-")
    name=b[0]
    work_time=int(b[1])
    #print(name)
    dict_robots[name]={}
    dict_robots[name][work]=work_time
    dict_robots[name][status]=1
    dict_robots[name]["end_time"]=-1
#print(dict_robots)



start_time=input()# start time give
while True:
    prod=input()
    if prod=="End":
        break
    products.append(prod)

current_time=start_time
counter_sec=0
find=False
while True:
    counter_sec += 1
    if len(products) < 1:
        break
    current_time = get_sec_from_TIME(start_time, counter_sec) # +1 2 3
    item=products.popleft()




    for robot in dict_robots: # checking for free robots on the line
        if int(only_sec(current_time)) >= int(dict_robots[robot]["end_time"]):
            dict_robots[robot]["end_time"]=only_sec(get_sec_from_TIME(current_time,dict_robots[robot][work]))
            print(f"{robot} - {item} [{current_time}]")
            break


    else: # "find some item in the iterable, else if none was found do ..."
       products.append(item)







#print("done")
