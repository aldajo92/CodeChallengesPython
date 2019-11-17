def return_operator(value1, value2):
    if value1 > value2:
        return ">"
    elif value1 < value2:
        return "<"
    else:
        return "="


for _ in range(int(input())):
    values = input().split(" ")
    print(return_operator(int(values[0]), int(values[1])))
