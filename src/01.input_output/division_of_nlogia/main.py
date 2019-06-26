def analyze_region(x_ref, y_ref, x, y):
    if x == x_ref or y == y_ref:
        return "divisa"
    elif y > y_ref:
        if x > x_ref:
            return "NE"
        else:
            return "NO"
    else:
        if x > x_ref:
            return "SE"
        else:
            return "SO"


entries_size = int(input())

while entries_size > 0:
    x_ref, y_ref = input().split(" ")
    for _ in range(entries_size):
        x, y = input().split(" ")
        print(analyze_region(int(x_ref), int(y_ref), int(x), int(y)))
    entries_size = int(input())
