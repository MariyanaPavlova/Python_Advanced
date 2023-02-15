from collections import deque

def convert_str_to_sec(str_time):
    hours, min, sec =[int(x) for x in str_time.split(":")]
    return hours*60*60 + min*60 + sec

def convert_sec_to_str_time(sec):
    sec %= 24*60*60
    hours = sec // (60*60)
    sec %= (60*60)
    min = sec // 60
    sec %= 60
    return f'{hours:02d}:{min:02d}:{sec:02d}'


robot_data = input().split(';')

proc_time_by_robot = {}
busy_until_by_robot = {}

for i in robot_data:
    com = i.split('-')
    name = com[0]
    proc_time = com[1]
    #name, proc_time = i.split('-')
    proc_time_by_robot[name] = int(proc_time)
    busy_until_by_robot[name] = -1

time = convert_str_to_sec(input())
items = deque()

while True:
    line = input()
    if line == "End":
        break
    items.append(line)

while items:
    time += 1
    item = items.popleft()

    for name, busy_until in busy_until_by_robot.items():
        if time >= busy_until:
            busy_until_by_robot[name] = time + proc_time_by_robot[name]
            print(f'{name} - {item} [{convert_sec_to_str_time(time)}]')
            break
    else:
        items.append(item)


