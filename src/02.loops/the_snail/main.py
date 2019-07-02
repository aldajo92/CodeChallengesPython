input_data = input()

while input_data != "0 0 0 0":
    h_ref, u_ref, d_ref, f = [int(x) for x in input_data.split(" ")]

    h = 100 * h_ref
    u = 100 * u_ref
    d = 100 * d_ref

    day = 1
    factor_climbed = f * u_ref
    distance_climbed = 0

    fatigue_factor = u

    while True:
        distance_climbed += fatigue_factor

        if fatigue_factor > 0:
            fatigue_factor -= factor_climbed

        if distance_climbed > h:
            break

        distance_climbed -= d

        if distance_climbed < 0:
            break

        day += 1

    if distance_climbed < 0:
        print("failure on day {}".format(day))
    else:
        print("success on day {}".format(day))

    input_data = input()
