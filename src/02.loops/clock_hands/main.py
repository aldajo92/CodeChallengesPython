read_input = input()

while read_input != "0:00":
    hours, minutes = read_input.split(":")
    h = int(hours)
    m = int(minutes)

    grade_hours = (h * 30) + (5 * m) / 10
    grade_minutes = m * 6

    total1 = grade_hours - grade_minutes

    if total1 < 0:
        total1 = -total1

    total2 = 360 - total1

    if total1 < total2:
        print("{0:.3f}".format(total1))
    else:
        print("{0:.3f}".format(total2))

    read_input = input()
