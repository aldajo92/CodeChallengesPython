def calculate_speed(raw_speeds, case):
    speeds = raw_speeds.split(" ")
    max_speed = 0
    for speed in speeds:
        int_speed = int(speed)
        if int_speed > max_speed:
            max_speed = int_speed
    return "Case {}: {}".format(case, max_speed)


for i in range(int(input())):
    print(calculate_speed(input(), i + 1))
