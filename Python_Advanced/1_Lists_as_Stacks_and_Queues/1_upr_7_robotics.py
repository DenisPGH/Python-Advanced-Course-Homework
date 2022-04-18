from collections import deque
products=deque()
class Robot():
    def __init__(self,info:str,start:str, curent_time:str,get=None): # info robot, start time
        info_parts=info.split("-")
        self.name=info_parts[0]
        self.working_time=int(info_parts[1])
        self.start=start
        self.curent_time=curent_time
        self.get=get
    def name_robot(self):
        return self.name

    def free_at(self): # return when  the robot is finish
        return get_sec_from_TIME(self.start,self.working_time)



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


robots=[str(x) for x in input().split(";")] # get the robots
dict_robots={}

work="work"
status="status"
for a in robots:
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

counter_sec=1
while True:

    if len(products)<1:
        break

    for robot in robots: # checking for free robots

        current_time = get_sec_from_TIME(start_time, counter_sec)
        #print(current_time)
        current_robot = Robot(robot, start_time, current_time)
        last_name=current_robot.name_robot()
        #start_time = current_time
        if dict_robots[current_robot.name_robot()][status]==1: # if the robot is free get the produkt
            # start_time=current_time
            dict_robots[current_robot.name_robot()]["end_time"]= get_sec_from_TIME(get_sec_from_TIME(current_time,-1), dict_robots[current_robot.name_robot()][work])

            print(f"{current_robot.name_robot()} - {products.popleft()} [{current_time}]")
            dict_robots[current_robot.name_robot()][status] =0



        elif dict_robots[current_robot.name_robot()]["end_time"] == current_time:
            dict_robots[current_robot.name_robot()][status] = 1


        counter_sec += 1

    products.rotate(1)




    if counter_sec > 32:
        break



