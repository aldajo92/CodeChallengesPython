input_data = input()

while input_data != "0 0 0 0":
    h, u, d, f = [int(x) for x in input_data.split(" ")]

    day = 0
    distance = 0.0
    factor_climbed = (f * u) / 100.00000
    reducer_climber = 0.0

    print("factor of {}".format(factor_climbed))

    while 0 <= distance <= h:
        print("distance morning: {};".format(distance))
        distance_per_day = u - reducer_climber

        if distance_per_day < 0:
            distance_per_day = 0
        distance += distance_per_day
        day += 1

        print("distance: {}; reducer: {}".format(distance, reducer_climber))
        if distance > h or distance <= 0:
            break

        reducer_climber += factor_climbed
        distance = distance - d

    if distance <= 0:
        print("failure on day {}".format(day))
    else:
        print("success on day {}".format(day))

    input_data = input()
