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
    dict_robots[name]["end_time"]=0
#print(dict_robots)



start_time=input()# start time give
while True:
    prod=input()
    if prod=="End":
        break
    products.append(prod)

current_time=start_time
counter_sec=1
find=False
while True:
    current_time = get_sec_from_TIME(start_time, counter_sec) # +1 2 3

    if len(products)<1:
        break

    for robot in dict_robots: # checking for free robots on the line

        #print(current_time)
        last_name=robot
        #start_time = current_time
        if dict_robots[robot][status]==1: # if the robot is free
            # start_time=current_time
            if last_name != robot :
                dict_robots[robot]["end_time"]= get_sec_from_TIME(get_sec_from_TIME(current_time,0), dict_robots[robot][work])
            elif last_name==robot :
                dict_robots[robot]["end_time"]= get_sec_from_TIME(get_sec_from_TIME(current_time,-1), dict_robots[robot][work])

            print(f"{robot} - {products.popleft()} [{current_time}]")
            dict_robots[robot][status] =0 # make the robot busy status
            find=True
            break # stop looping in the robots




        if dict_robots[robot]["end_time"] == current_time:
            dict_robots[robot]["end_time"]=0
            dict_robots[robot][status] = 1
        #counter_sec += 1

    else: # "find some item in the iterable, else if none was found do ..."
       products.rotate(-1)

    counter_sec += 1

    #products.rotate(-1)





#print("done")
